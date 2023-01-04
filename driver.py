# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as BraveService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.utils import ChromeType

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_argument('--log-level=3'

# # Create new automated instance of Chrome
# driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@st.experimental_singleton
def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

driver = get_driver()
