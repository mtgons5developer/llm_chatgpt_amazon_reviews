guidelines_prompt = '''
''Does the following review comply with all 14 of Amazon's guidelines? If not, which guideline(s) does it potentially violate?

    1- Seller, Order, or Shipping Feedback:
    Reviews and Questions and Answers should focus on the product itself rather than individual experiences related to sellers, ordering, or shipping.
    - Avoid discussing the following topics in reviews and questions and answers:
    - Seller performance and customer service.
    - Ordering issues, returns, and refunds.
    - Shipping packaging.
    - Product condition and damage caused during shipping.
    - Shipping cost and delivery speed.
    Why? The purpose of community content is to provide information about the product. While we value feedback on sellers and packaging, we encourage you to share such feedback through appropriate channels other than reviews or questions and answers.\n

    2- Comments about Pricing or Availability:
    It is acceptable to comment on pricing if it directly relates to the product's value. For example, "This blender is excellent for only $29."
    - Comments regarding pricing based on individual experiences are not permitted. For example, "I found this product $5 cheaper at my local store."
    - Such comments are irrelevant to all customers and therefore not allowed.
    - Certain comments about availability are allowed, such as expressing a desire for a product to be available in a different format, like paperback for a book.
    - However, comments specific to availability at a particular store are not permitted.
    The community's purpose is to share product-specific feedback that will be relevant to all customers.\n

    3- Content written in unsupported languages:
    Supported languages for content are English and Spanish.
    It should only be written in English or Spanish.\n

    4- Repetitive Text, Spam, or Pictures Created with Symbols:
    Contributions with distracting content and spam are not allowed.
    This includes:
    - Repetitive text that serves no meaningful purpose.
    - Nonsense, gibberish, or content that lacks coherence.
    - Content consisting solely of punctuation marks and symbols.
    - ASCII art, which refers to pictures created using symbols and letters.
    Why? The purpose of contributions is to provide helpful and relevant information to the community. Repetitive text, spam, and content that lacks substance or meaningful value detract from the overall usefulness and readability of the platform.\n

    5- Private Information:
    Do not post content that invades others' privacy or shares your own personal information.
    This includes, but is not limited to:
    - Phone numbers
    - Email addresses
    - Mailing addresses
    - License plate numbers
    - Data source names (DSN)
    - Order numbers
    Why? Respecting privacy is crucial to maintain a safe and secure environment. Sharing personal information can lead to unintended consequences or potential misuse. Please refrain from posting any content that compromises privacy, both yours and others'.\n

    6- Profanity or Harassment:
    While questioning others' beliefs and expertise is acceptable, it's important to maintain a respectful tone.
    The following actions are not allowed:
    - Using profanity, obscenities, or engaging in name-calling.
    - Engaging in harassment or making threats.
    - Launching personal attacks on individuals with whom you disagree.
    - Posting content that constitutes libel, defamation, or is deliberately inflammatory.
    - Drowning out others' opinions by posting from multiple accounts or coordinating with others.
    Why? Promoting a respectful and inclusive environment fosters constructive discussions. Avoiding profanity, harassment, and personal attacks ensures that conversations remain civil and beneficial for everyone involved.\n

    7- Hate Speech:
    Expressing hatred towards individuals based on their characteristics is strictly prohibited.
    This includes but is not limited to:
    - Race
    - Ethnicity
    - Nationality
    - Gender
    - Gender identity
    - Sexual orientation
    - Religion
    - Age
    - Disability
    Additionally, promoting organizations that propagate hate speech based on these characteristics is also not allowed.
    Why? Creating a safe and inclusive environment is paramount. By disallowing hate speech and the promotion of such organizations, we ensure that our platform remains respectful, tolerant, and free from discrimination.\n

    8- Sexual Content:
    Discussions regarding sex and sensuality products available on Amazon are permissible.
    Likewise, products containing sexual content such as books and movies can be discussed.
    However, the following restrictions apply:
    - Profanity and obscene language are not allowed.
    - Content containing nudity or sexually explicit images or descriptions is prohibited.
    Why? Allowing discussions about sex-related products while maintaining a respectful atmosphere is essential. By prohibiting profanity, explicit images, and descriptions, we ensure that the community remains appropriate and comfortable for all users.\n

    9- External Links:
    - Links to other products on Amazon are permitted, but linking to external sites is not allowed.
    - Avoid posting links to phishing or malware-infected websites.
    - Refrain from sharing URLs that include referrer tags or affiliate codes.
    Why? Allowing links to other products on Amazon enables users to access additional information. However, prohibiting external links ensures the safety and security of our community by preventing potential malicious content or unauthorized tracking through referrer tags and affiliate codes.\n

    10- Ads or Promotional Content:
    - Do not post content that primarily serves the purpose of promoting a company, website, author, or special offer.
    - Contributions should focus on providing genuine and helpful information rather than promotional material.
    Why? The primary objective of the community is to facilitate informative discussions and share knowledge. By discouraging ads or promotional content, we ensure that the platform remains focused on valuable contributions rather than overt advertising.\n

    11- Conflicts of Interest:
    Creating, editing, or posting content about your own products or services is strictly prohibited.
    The same restriction applies to content related to products or services offered by:
    - Friends
    - Relatives
    - Employers
    - Business associates
    - Competitors
    Why? Upholding a fair and unbiased environment is crucial. By avoiding conflicts of interest, we maintain the integrity and authenticity of the community's content, ensuring that discussions are driven by genuine experiences and unbiased perspectives.\n

    12- Solicitations:
    When requesting others to post content about your products, ensure that the request remains neutral. Influencing them to leave a positive rating or review is not allowed.
    Offering, requesting, or accepting compensation for creating, editing, or posting content is strictly prohibited. Compensation includes free and discounted products, refunds, reimbursements, and any attempts to manipulate the Amazon Verified Purchase badge through special pricing or reimbursements for reviewers.
    If you have a financial or close personal connection to a brand, seller, author, or artist:
    - Posting content other than reviews and questions and answers is acceptable, but it is essential to clearly disclose your connection.
    - Brands or businesses cannot engage in activities that divert Amazon customers to non-Amazon websites, applications, services, or channels. This includes ads, special offers, and "calls to action" designed to conduct marketing or sales transactions. Additional labeling is not necessary if you post content about your own products or services through a brand, seller, author, or artist account.
    - Authors and publishers can still provide readers with free or discounted copies of their books as long as they do not require a review in exchange or attempt to influence the review.
    Why? Maintaining transparency, fairness, and unbiased opinions is fundamental to the integrity of the community. By discouraging solicitations and ensuring clear disclosure of connections, we foster an environment that promotes authentic engagement and trust among users.\n

    13- Plagiarism, Infringement, or Impersonation:
    Only post content on Amazon that you own or have proper permission to use. This includes text, images, and videos.
    The following actions are strictly prohibited:
    - Posting content that infringes on others' intellectual property rights, including copyrights, trademarks, patents, and trade secrets.
    - Engaging in interactions with community members that infringe on others' intellectual property or proprietary rights.
    - Impersonating individuals or organizations.
    Why? Respecting intellectual property rights and preventing impersonation is crucial to maintain a fair and trustworthy community. By discouraging plagiarism, infringement, and impersonation, we ensure that original content is shared, intellectual property is respected, and individuals are not misrepresented.\n

    14- Illegal Activities:
    Posting content that promotes or encourages illegal activities is strictly prohibited. This includes:
    - Violence
    - Illegal drug use
    - Underage drinking
    - Child or animal abuse
    - Fraudulent activities
    Content that advocates or threatens physical or financial harm to yourself or others, including terrorism, is not allowed. Jokes or sarcastic comments about causing harm are also prohibited.
    Offering fraudulent goods, services, promotions, or participating in schemes such as "make money fast" or pyramid schemes is not allowed.
    Encouraging the dangerous misuse of a product is strictly prohibited.
    Why? Upholding legal and ethical standards is of utmost importance. By prohibiting content that promotes illegal activities, harm, or fraud, we maintain a safe and trustworthy community where users can engage responsibly and contribute to meaningful discussions.\n

    Example training dataset:
    {fine_tune}\n

    Status: Compliant or Violation w/o additional content.
    If Status = Compliant then Reason = 'It doesn't violate any amazon guidelines'. If Status = Violation explain why it's in Violation of the said 14 guidelines.
    If Compliant set Result: 'NO' w/o additional content. If in Violation set Result: 'YES' w/o additional content. The "Result" is assigned as "Maybe" to convey uncertainty.END'''

'''
'''''''''