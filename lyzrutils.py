import streamlit as st
from PIL import Image

def filterData(data_in_json):
    filtered_data = []
    for person in data_in_json.get('people', []):
        filtered_info = {
            'name': person.get('name'),
            'email': person.get('email'),
            'linkedin_url': person.get('linkedin_url'),
            'headline': person.get('headline')
        }
        filtered_data.append(filtered_info)

    return {'people': filtered_data}

def demo_page_config(layout = "centered"):
    st.set_page_config(
        page_title="AI Prospect Generator",
        layout=layout,  # or "wide" 
        initial_sidebar_state="auto",
        page_icon="lyzr-logo-cut.png"
    )

def lyzr_demo_end(text = "This app uses Lyzr Core."):
    with st.expander("ℹ️ - About this App"):
        st.markdown(f"""
        {text} For any inquiries or issues, please contact Lyzr.
        """)
        st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
        st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
        st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
        st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)

def lyzr_demo_start(main = False):
    image = Image.open("lyzr-logo.png")
    st.image(image, width=150)
    if main:
        # App title and introduction
        st.title("AI Prospect Generator")
        st.markdown("### Welcome to the AI Prospect Generator!")
        st.markdown("Generate prospects with just your product description")
        # st.markdown("#### (Start with an emoji here) Clear short instruction")
        st.caption('Note: Products with a huge audience naturally have higher prospects!')