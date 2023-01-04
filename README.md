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
  pip install requirements.txt
```

Start the server

```bash
  streamlit run app.py
```


## Screenshots

![App Screenshot]()


## Authors

- [@aditya-gupta-04](https://github.com/aditya-gupta-04)
- [@aryanlath](https://github.com/aryanlath)
- [@devansh-bhardwaj](https://github.com/devansh-bhardwaj)
- [@SpyzzVVarun](https://github.com/SpyzzVVarun)
