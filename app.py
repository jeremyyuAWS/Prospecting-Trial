from lyzragents import askLyzrAgent
from lyzrpeoplesearch import writeToFile, searchPeople
from lyzrfilterdict import getDict
from lyzrutils import *
import json
import streamlit as st



demo_page_config()
lyzr_demo_start(main=True)
query = st.text_input("Enter Your Query Here")
buttonBool = st.button("Submit Query")



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

    #Streamlit UI
    st.markdown("""
        <style>
        .card {
            background-color: #f9f9f9;
            padding: 15px;
            margin: 10px 0;
            border-radius: 8px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            height: 200px
        }
        .card h3 {
            margin: 0;
            font-size: 1.2em;
            color: #333;
        }
        .card p {
            margin: 5px 0;
            font-size: 0.9em;
            color: #666;
        }
        .card a {
            color: #0073b1;
            text-decoration: none;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    # Split the layout into two columns
    col1, col2 = st.columns(2)

    for i, person in enumerate(filtered_data["people"]):
        column = col1 if i % 2 == 0 else col2
        column.markdown(f"""
            <div class="card">
                <h3>{person['name']}</h3>
                <p>{person['headline']}</p>
                <p>Email: <a href="mailto:{person['email']}">{person['email']}</a></p>
                <p>LinkedIn: <a href="{person['linkedin_url']}" target="_blank">View Profile</a></p>
            </div>
        """, unsafe_allow_html=True)

lyzr_demo_end(text="Unlock the potential of AI-driven prospecting with our app, designed to seamlessly generate and refine high-value leads tailored to your business needs. This app was built using Lyzr Agents")