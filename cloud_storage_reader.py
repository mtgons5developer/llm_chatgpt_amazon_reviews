import os
import csv
import time
import psycopg2
import traceback

from langchain import OpenAI, LLMChain
from langchain.chat_models import ChatOpenAI

from google.cloud import storage
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = openai_api_key

# Retrieve the PostgreSQL connection details from environment variables
db_host = os.getenv('HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DATABASE')
db_user = os.getenv('USER')
db_password = os.getenv('PASSWORD')

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_password
)

def read_file_from_gcs(bucket_name, file_name):
    # Instantiate the client
    client = storage.Client()

    # Retrieve the bucket and file
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Download the file's content as a string
    content = blob.download_as_text()

    return content

try:

    # Provide the name of your bucket and the file you want to read
    bucket_name = "schooapp2022.appspot.com"
    file_name = "csv-gpt.csv"

    # Read the file from Google Cloud Storage
    file_content = read_file_from_gcs(bucket_name, file_name)

    # Parse the CSV content
    rows = csv.reader(file_content.splitlines())
    header = next(rows)  # Extract the header row
    # print("CSV Header:", header)  # Print the header for debugging

    # Find the indices of the required columns
    column_indices = [header.index(column) for column in ["Title", "Body", "gpt_status", "gpt_reason"]]

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query to retrieve the guidelines_prompt from the database
    query = "SELECT guidelines FROM guidelines_prompt WHERE id = 4;"
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()

    # Extract the guidelines_prompt from the result
    guidelines_prompt = result[0]

    # Iterate over the rows and extract the required columns
    for row in rows:
        columns = [row[index] for index in column_indices]
        title, body, gpt_status, gpt_reason = columns
        # Do something with the extracted columns
        review = f"{title}, {body}"
        # Create a dictionary with the extracted values
        result = {'review': review, 'status': gpt_status, 'reason': gpt_reason}
        # Convert the dictionary to a list
        examples = [result]

        example_prompt = PromptTemplate(input_variables=["review", "status", "reason"],
                                        template="Review: '''{review}'''\nStatus: {status}\nReason: {reason}")

        few_shot_template = FewShotPromptTemplate(
            examples=examples,
            example_prompt=example_prompt,
            prefix=guidelines_prompt,
            suffix="Review: '''{input}'''\nStatus:",
            input_variables=["input"]
        )

        chat_llm = ChatOpenAI(temperature=0)
        llm_chain = LLMChain(llm=chat_llm, prompt=few_shot_template)

        answer = llm_chain.run(review)
        # print(f"Review: {review}\nStatus: {answer.strip()}")

        # Split the contents into status and reason
        status, reason = answer.strip().split('\nReason: ', 1) if '\nReason: ' in answer else (answer, '')

        # Insert the extracted values into the 'analysis' table
        insert_query = """
            INSERT INTO analysis (review, status, reason)
            VALUES (%s, %s, %s)
        """
        values = (review, status, reason)  # Assuming you have the 'review' value

        cursor.execute(insert_query, values)
        conn.commit()
        print(f"Review: {review}\nStatus: {answer.strip()}")

except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)
    traceback.print_exc()

finally:
    # Close the connection
    if conn is not None:
        conn.close()
        cursor.close()

        # Check if the 'analysis' table exists
        # check_table_query = """
        #     SELECT EXISTS (
        #         SELECT 1
        #         FROM information_schema.tables
        #         WHERE table_name = 'analysis'
        #     )
        # """
        # cursor.execute(check_table_query)
        # table_exists = cursor.fetchone()[0]

        # Create the 'analysis' table if it doesn't exist
        # if not table_exists:
        #     create_table_query = """
        #         CREATE TABLE analysis (
        #             id SERIAL PRIMARY KEY,
        #             review TEXT,
        #             status TEXT,
        #             reason TEXT
        #         )
        #     """
        #     cursor.execute(create_table_query)
        #     conn.commit()


# # Use the executemany() method: Instead of executing individual INSERT statements for each row, you can use the executemany() 
# # method to insert multiple rows at once. This can significantly improve the insertion speed. Modify the code as follows:
    
# # Create a list to hold the values for multiple rows
# rows_to_insert = []

# # Iterate over the rows and extract the required columns
# for row in rows:
#     columns = [row[index] for index in column_indices]
#     title, body, gpt_status, gpt_reason = columns
#     # Do something with the extracted columns
#     review = f"{title}, {body}"
#     # Create a dictionary with the extracted values
#     result = {'review': review, 'status': gpt_status, 'reason': gpt_reason}
#     # Convert the dictionary to a tuple and append it to the list
#     rows_to_insert.append((review, gpt_status, gpt_reason))

# # Insert the extracted values into the 'analysis' table
# insert_query = """
#     INSERT INTO analysis (review, status, reason)
#     VALUES (%s, %s, %s)
# """
# cursor.executemany(insert_query, rows_to_insert)
# conn.commit()

# # Use a with statement for the cursor: Instead of manually closing the cursor, you can use a with statement to handle the 
# # cursor automatically. This ensures that the cursor is properly closed even if an exception occurs. Modify the code as follows:

# # Create a cursor object to execute SQL queries
# with conn.cursor() as cursor:
#     # ... existing code ...

#     # Insert the extracted values into the 'analysis' table
#     cursor.executemany(insert_query, rows_to_insert)
#     conn.commit()
