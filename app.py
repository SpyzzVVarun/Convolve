from parsing import parsePage
from links import *
import streamlit as st
import json
from json2html import *
import os
from fuzzywuzzy import process

def clear_text():
    st.session_state["text1"] = ""
    st.session_state["text2"] = ""
    st.session_state["text3"] = ""
    st.session_state["text4"] = ""
    st.session_state["text5"] = ""

def addFeatures(option):
    if option == 'Direct Web Page':
        os_name = st.text_input('Enter OS', key = "text1")
        url = st.text_input('Enter Web Page URL', key = "text2")
        
    elif option == 'Config Guide Link (Beta Testing)':
        os_name = st.text_input('Enter OS', key = "text3")
        url = st.text_input('Enter Config Guide URL', key = "text4")

    bt1 = st.button("Update Database")

    if (bt1):
        try:
            os.mkdir(f"databases/{os_name}/")
        except:
            pass
        if option == 'Config Guide Link (Beta Testing)':
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
        bt4 = st.button("Re-Run", on_click=clear_text)

st.title('Cisco Config Guides Databases')

option1 = st.sidebar.radio("Update Database or View Database?", ("Update", "View"))


if option1 == "Update":
    option2 = st.radio("How would you like to add features?", ("Direct Web Page", "Config Guide Link (Beta Testing)"))
    addFeatures(option2)

elif option1 == 'View':
    os_name = st.text_input('Enter OS', key = "text")
    user_input = st.text_input('Enter feature name', key = "text")
    bt2 = st.button("Search")
    btextra = st.button("View Full Database")
    if (bt2):
        if os.path.exists(f"databases/{os_name}/configs.json"):
            with open(f"databases/{os_name}/configs.json", "r") as f:
                feature_configs = json.load(f)
            
            choices = feature_configs.keys()
            display_dict = dict()   
            for ele in process.extract(user_input, choices):
                if ele[1] > 60:
                    display_dict[ele[0]] = feature_configs[ele[0]]
            if len(display_dict.keys()) < 5:
                for ele in process.extract(user_input, choices)[len(display_dict.keys()): 6]:
                    display_dict[ele[0]] = feature_configs[ele[0]]

            json_object = json.dumps(display_dict, indent = 4)
            html_code = json2html.convert(json = json_object)
            st.markdown(html_code, unsafe_allow_html=True)
            bt3 = st.button("Reset", on_click=clear_text)

    elif (btextra):
        if os.path.exists(f"databases/{os_name}/configs.json"):
            with open(f"databases/{os_name}/configs.json", "r") as f:
                feature_configs = json.load(f)

            json_object = json.dumps(feature_configs, indent = 4)
            html_code = json2html.convert(json = json_object)
            st.markdown(html_code, unsafe_allow_html=True)
            bt3 = st.button("Reset", on_click=clear_text)
