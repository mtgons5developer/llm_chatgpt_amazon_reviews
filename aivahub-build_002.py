import os
import json
import psycopg2

from langchain import OpenAI, LLMChain
from langchain.chat_models import ChatOpenAI
from g_sheet import sheet
from create_env import create
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

def create_table():
    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # Get the spreadsheet name
    spreadsheet_name = sheet()

    # Remove any special characters from the spreadsheet name to use as a table name
    table_name = "".join(c for c in spreadsheet_name if c.isalnum())

    # Create the table if it doesn't exist
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id SERIAL PRIMARY KEY,
        title TEXT,
        body TEXT,
        gpt_status TEXT,
        gpt_reason TEXT
    );
    """
    cur.execute(create_table_query)
    conn.commit()

    # Close the cursor
    cur.close()

def openAI():
    #Build_002 Anaylze Title and Body only
    try:
        # Create a cursor object to execute SQL queries
        cur = conn.cursor()

        # Fetch the first row from the table
        cur.execute(f"SELECT title, body, gpt_status, gpt_reason FROM {table_name} LIMIT 1")
        row = cur.fetchone()

        if row:
            # Combine the title and body columns with a comma separator
            review = f"{row[0]}, {row[1]}"
            # status = row[2]
            # reason = row[3]

            # Create a dictionary with the extracted values
            result = {'review': review}#, 'status': status}#, 'reason': reason}
            # Convert the dictionary to a list
            examples = [result]

            example_prompt = PromptTemplate(input_variables=["review"],
                                            template="Review: '''{review}")

            # Execute the query to retrieve the guidelines_prompt from the database
            query = "SELECT guidelines FROM guidelines_prompt WHERE id = 4;"
            cur.execute(query)

            # Fetch the result
            result = cur.fetchone()

            # Extract the guidelines_prompt from the result
            guidelines_prompt = result[0]

            few_shot_template = FewShotPromptTemplate(
                examples=examples,
                example_prompt=example_prompt,
                prefix=guidelines_prompt,
                suffix="Review: '''{input}",
                input_variables=["input"]
            )

            # completion_llm = OpenAI(temperature=0.0)
            chat_llm = ChatOpenAI(temperature=0.8)
            llm_chain = LLMChain(llm=chat_llm, prompt=few_shot_template)

            answer = llm_chain.run(review)

            print(f"Review: {review}\nStatus: {answer.strip()}")

        else:
            print("No rows found in the table.")

        # Close the cursor
        cur.close()

    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)

    finally:
        # Close the connection
        if conn is not None:
            conn.close()

create_table()
openAI()
