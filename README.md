# Sentiment-Analysis

# How to run?
### requirements are listed in requirements.txt just pip install that inside a virtual environment
### run the instance of mongodb server
### <code> mongod --dbpath="{path_to_the_database}" (Note: I have included all my database under database/mongodb_database)
### all the analysis is done by sentimentAPI.py
### sentimentAPI is a REST api, upon request it streams tweets in new thread and perform analysis
### so run the sentimentAPI with <code> python sentimentAPI.py </code>
### app.py is client app that requests sentimentAPI for the analysis, and shows the real time analysis while streaming from twitter uing web-sockets in a spline graph
### run app.py <code> python app.py </code>
### use url <code> http://localhost:5000 </code> to use the app

# How does it look?
![home](https://user-images.githubusercontent.com/11765482/37170379-c8e97afc-2332-11e8-9872-3f43f24ce5bb.PNG)
![categories](https://user-images.githubusercontent.com/11765482/37170389-cdfd6fda-2332-11e8-9e5d-b6cfc31ef2a0.PNG)
![livesentiment3png](https://user-images.githubusercontent.com/11765482/37170406-d4f18ad8-2332-11e8-9195-0bd42d195f1b.PNG)
![histroy](https://user-images.githubusercontent.com/11765482/37170415-d8f7bddc-2332-11e8-96bb-df58adbad1d4.PNG)
![about](https://user-images.githubusercontent.com/11765482/37170419-db765fc8-2332-11e8-87d8-fb7dbc2a431c.PNG)
![livesentiment2](https://user-images.githubusercontent.com/11765482/37170428-e4b15b6a-2332-11e8-975a-a677789506b0.PNG)
