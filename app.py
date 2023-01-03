from parsing import parsePage
from links import *
import streamlit as st
import json
from json2html import *
import os

def addFeatures(option):
    if option == 'Direct Web Page':
        os_name = st.text_input('Enter OS')
        url = st.text_input('Enter Web Page URL')
        
    elif option == 'Config Guide Link':
        os_name = st.text_input('Enter OS')
        url = st.text_input('Enter Config Guide URL')

    bt1 = st.button("Update Database")

    if (bt1):
        try:
            os.mkdir(f"databases/{os_name}/")
        except:
            pass
        if option == 'Config Guide Link':
            links = get_landing_links(url)
        else:
            links = [url]
        feature_configs = parsePage(links)

        try:
            with open(f"databases/{os_name}/configs.json", "r") as f:
                old_dict = json.load(f)
                f.close()
        except:
            old_dict = dict()

        old_dict.update(feature_configs)

        with open(f"databases/{os_name}/configs.json", "w") as f:
            json.dump(old_dict, f)
            f.close()
        st.success("Updated Database")

st.title('Cisco Config Guides Databases')

option1 = st.sidebar.radio("Update Database or View Database?", ("Update", "View"))


if option1 == "Update":
    option2 = st.radio("How would you like to add features?", ("Direct Web Page", "Config Guide Link"))
    addFeatures(option2)

elif option1 == 'View':
    os_name = st.text_input('Enter OS')
    if os.path.exists(f"databases/{os_name}/configs.json"):
        with open(f"databases/{os_name}/configs.json", "r") as f:
            feature_configs = json.load(f)
        json_object = json.dumps(feature_configs, indent = 4)
        html_code = json2html.convert(json = json_object)
        st.markdown(html_code, unsafe_allow_html=True)
