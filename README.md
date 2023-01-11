# Convolve

# Config Search DataBase

A ML/NLP model to parse through any
webpage(config guide link) and extract each feature to their configs and
store it in DB. DB has to be separately created for each OS type(IOS/IOS-XE,
IOS XR, Nexus.. etc).
The model has been deployed and accepts both config guide links and direct page links to store each feature along with the OS in the database.


## Run Locally

Clone the project

```bash
  git clone https://github.com/SpyzzVVarun/Convolve.git
```

Go to the project directory

```bash
  cd Convolve
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run app.py
```
Note: \
You must have Chrome installed to run the app.


## Screenshots

![App Screenshot](https://github.com/aryanlath/Convolve/blob/Updated/images/Screenshot%202023-01-04%20at%2010.10.52%20PM.png)
![App Screenshot](https://github.com/aryanlath/Convolve/blob/Updated/images/Screenshot%202023-01-04%20at%2010.10.21%20PM.png?raw=true)

## Features

If you want to observe the automated Google tab you can uncomment the following line from driver.py file. 

```bash
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as BraveService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.utils import ChromeType

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_argument('--log-level=3'

# # Create new automated instance of Chrome
# driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)
```

and comment the these lines

```bash
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
```


## Authors

- [@SpyzzVVarun](https://github.com/SpyzzVVarun)
- [@aditya-gupta-04](https://github.com/aditya-gupta-04)
- [@aryanlath](https://github.com/aryanlath)
- [@devansh-bhardwaj](https://github.com/devansh-bhardwaj)

