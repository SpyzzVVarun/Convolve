from parsing import parsePage
from links import *
import streamlit as st
import json
import os

st.title('Cisco Config Guides Databases')
option = st.selectbox(
        "How would you like to add features?",
        ("Direct Web Page", "Config Guide Link"))
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
    json_object = json.dumps(feature_configs, indent = 4) 
    with open(f"databases/{os_name}/configs.json", "a") as f:
        f.write(json_object)
        f.close()
        st.success("Updated Database")