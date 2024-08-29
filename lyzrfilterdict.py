from openai import OpenAI
import os

def getDict(prompt):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": "You create filters for apollo.io based on user input. Convert what ever possible filters you can make using the guide below.\n\nYour job is to assess the Ideal Customer Profile and other information provided and create filters which will then later be used on Apollo.io. \n\nFormat for the below data.\n\nParameter : Example // Description\n\n{\n  \"person_titles\": [\"sales director\", \"engineer manager\"],  // optional, an array of the person's titles. Apollo will return results matching ANY of the titles passed in.\n  \"q_keywords\": \"Tim\",  // optional, a string of words over which we want to filter the results.\n  \"prospected_by_current_team\": [\"no\"],  // optional, an array of string booleans defining whether to look in net new database only (\"no\") or see saved contacts only (\"yes\").\n  \"person_locations\": [\"California, US\", \"Minnesota, US\"],  // optional, an array of strings denoting allowed locations of the person.\n  \"person_seniorities\": [\"senior\", \"manager\"],  // optional, an array of strings denoting the seniorities or levels.\n  \"contact_email_status\": [\"verified\", \"guessed\", \"unavailable\", \"bounced\", \"pending_manual_fulfillment\"],  // optional, an array of strings to look for people having a set of email statuses.\n  \"q_organization_domains\": \"google.com\\nfacebook.com\",  // optional, an array of the company domains to search for, joined by the new line character.\n  \"organization_locations\": [\"California, US\", \"Minnesota, US\"],  // optional, an array of strings denoting allowed locations of organization headquarters of the person.\n  \"organization_ids\": [\"63ff0bc1ff57ba0001e7eXXX\"],  // optional, an array of organization ids obtained from companies-search.\n  \"organization_num_employees_ranges\": [\"1,10\", \"101,200\"],  // optional, an array of intervals to include people belonging in an organization having a number of employees in a range.\n  \"page\": 1,  // optional, an integer that allows you to paginate through the results.\n  \"per_page\": 10  // optional, an integer to load per_page results on a page. Should be in the inclusive range [1, 100].\n}\n\nYou have to create filters based on this priority:\n1. person_titles\n2. person_locations\n3. q_organization_domains (if mentioned in the user input)\n\nAnything apart from these 3 should only be used if the ideal customer profile is niche or explicitly calls for it.\n\nAdditional instructions: Default to 500 page and 100 per page unless instructed otherwise. Make sure the output is in JSON format. Make sure the filters are vague enough to ensure not missing out on potential clientele. Organization revenue should be vague always, never assume only high revenue companies can afford potentially higher priced items. Unless really needed do not use person_seniorities. Use states or cities for location, just like how companies put on LinkedIn."
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": prompt
            }
        ]
        }
    ],
    temperature=1,
    max_tokens=4095,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={
        "type": "json_object"
    }
    )
    response_data = response.dict()
    return response_data['choices'][0]['message']['content']  
