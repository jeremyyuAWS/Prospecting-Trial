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
            "text": "You create filters for apollo.io based on user input. Convert what ever possible filters you can make using the guide below\n\nFormat for the below data. Parameter\tDescription\tExample\n\n```\nperson_titles (optional)\tAn array of the person's title. Apollo will return results matching ANY of the titles passed in\t[\"sales director\", \"engineer manager\"]\nq_keywords (optional)\tA string of words over which we want to filter the results\t\"Tim\"\nprospected_by_current_team (optional)\tAn array of string booleans defining whether we want models prospected by current team or not. \"no\" means to look in net new database only, \"yes\" means to see saved contacts only\t[\"no\"]\nperson_locations (optional)\tAn array of strings denoting allowed locations of the person\t[\"California, US\", \"Minnesota, US\"]\nperson_seniorities (optional)\tAn array of strings denoting the seniorities or levels\t[\"senior\", \"manager\"]\ncontact_email_status (optional)\tAn array of strings to look for people having a set of email statuses\t[\"verified\", \"guessed\", \"unavailable\", \"bounced\", \"pending_manual_fulfillment\"]\nq_organization_domains (optional)\tAn array of the company domains to search for, joined by the new line character.\t\"google.com\\nfacebook.com\"\norganization_locations (optional)\tAn array of strings denoting allowed locations of organization headquarters of the person\t[\"California, US\", \"Minnesota, US\"]\norganization_ids (optional)\tAn array of organization ids obtained from companies-search\t[\"63ff0bc1ff57ba0001e7eXXX\"]\norganization_num_employees_ranges (optional)\tAn array of intervals to include people belonging in an organization having number of employees in a range\t[\"1,10\", \"101,200\" ]\npage (optional)\tAn integer that allows you to paginate through the results\t1\nper_page (optional)\tAn integer to load per_page results on a page. Should be in inclusive range [1, 100]\t10\n```\n\nan example request would be \n```\n{\n    \"q_organization_domains\": \"apollo.io\\ngoogle.com\",\n    \"page\" : 1,\n    \"per_page\": 100,\n    \"organization_locations\": [\"California, US\"],\n    \"person_seniorities\": [\"senior\", \"manager\"],\n    \"organization_num_employees_ranges\": [\"1,1000000\"],\n    \"person_titles\" : [\"sales manager\", \"engineer manager\"]\n}\n```\n\nDefault to 500 page and 100 per page unless instructed otherwise. Make sure the output is in JSON format.\n Make sure the filters are vague enough to ensure not missing out on potential clientele. Organization revenue should be vague always, never assume only high revenue companies can afford potentially higher priced items. Unless really needed do not use person_seniorities. Use states or cities for location, just like how companies put on linkedin."
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
