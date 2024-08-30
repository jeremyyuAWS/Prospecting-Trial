from lyzragents import askLyzrAgent
from lyzrpeoplesearch import writeToFile, searchPeople
from lyzrfilterdict import getDict
from lyzrutils import *
import json
import streamlit as st



demo_page_config()
lyzr_demo_start(main=True)
query = st.text_input("Enter Your Product Details Here")
buttonBool = st.button("Generate Prospects")

if buttonBool and query:
    print("Step 1 - user query")
    with st.spinner("Scanning for Ideal Audience..."):
        target_audience = askLyzrAgent(query)
        print("Step 2 - target persona: " + target_audience)
        st.markdown("🔍 Audience Insights Unlocked!")
    if target_audience:
        with st.spinner("Engineering Precision Filters..."):
            data_dict_for_apollo = getDict(target_audience)
            print("Step 3 - data dict for apollo: " + str(data_dict_for_apollo))
            st.markdown("🎯 Precision Filters Ready for Deployment!")

        data_dict_for_apollo_as_dict = json.loads(data_dict_for_apollo)

        writeToFile(data_dict_for_apollo, "input")

        if data_dict_for_apollo_as_dict:
            with st.spinner("Discovering Top Prospects..."):
                data_in_json = searchPeople(data_dict_for_apollo_as_dict)
                print("Step 4 - full response: " + str(data_in_json))
                st.markdown("🚀 Top Prospects Ready for Action!")

            filtered_data = filterData(data_in_json)
            print("Filtered data: ")
            print(json.dumps(filtered_data, indent=4))

            # Check if the filtered data is empty and re-run searchPeople if needed
            while not filtered_data["people"]:
                print("Filtered data is empty. Re-running searchPeople...")
                with st.spinner("Reprocessing data..."):
                    data_dict_for_apollo = getDict(target_audience)
                    data_dict_for_apollo_as_dict = json.loads(data_dict_for_apollo)
                    data_in_json = searchPeople(data_dict_for_apollo_as_dict)
                    filtered_data = filterData(data_in_json)
                    print("Reattempted Filtered data: ")
                    print(json.dumps(filtered_data, indent=4))

            writeToFile(filtered_data, "output")

    if target_audience:
        with st.expander("Want to see the Target Customer Persona Report we built for you ?"):
            st.markdown(target_audience)

    st.markdown("""
        <style>
        .card {
            background-color: #ffffff;
            padding: 20px;
            margin: 10px 0;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            height: auto;
        }
        .card h3 {
            margin: 0;
            font-size: 1.5em;
            color: #333;
        }
        .card p {
            margin: 5px 0;
            font-size: 1em;
            color: #555;
        }
        .card a {
            color: #1a73e8;
            text-decoration: none;
            font-weight: 500;
        }
        </style>
    """, unsafe_allow_html=True)

    # Split the layout into two columns
    cols = st.columns(2)
    for index, person in enumerate(filtered_data["people"]):
        with cols[index % 2]:
            email = person.get('email')
            if email and email != "email_not_unlocked@domain.com":
                email_html = f'<p>Email: <a href="mailto:{email}">{email}</a></p>'
            else:
                email_html = "<p></p>"
            
            st.markdown(f"""
                <div class="card">
                    <h3>{person.get('name', 'N/A')}</h3>
                    <p>{person.get('headline', 'No headline available')}</p>
                    <p>LinkedIn: <a href="{person.get('linkedin_url', '#')}" target="_blank">View Profile</a></p>
                    {email_html}
                </div>
            """, unsafe_allow_html=True)

lyzr_demo_end(text="Unlock the potential of AI-driven prospecting with our app, designed to seamlessly generate and refine high-value leads tailored to your business needs. This app was built using Lyzr Agents")