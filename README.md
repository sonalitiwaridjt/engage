# engage-submission


## Introduction
- This app represents how Movie recommendations can work better with actual mood of the user.
- Even with metric such as RMSE and average reciprocal hit rank we definitely can not beat the results of online A/B tests. 
- We just cant simulate what goes on inside users' head. The real reactions are the ones which matter to determine what works and what doesn't.
- This is why this project speculates closely the current mood of the user and tries to recommend something which wwould be most likely to be liked by the user in that mood.


## How to detect mood?
- To detect mood there are numerous ways, such as trying to capture the face expressions, using speech emotion recognition,
- This project makes use of [Face-API](https://justadudewhohacks.github.io/face-api.js/docs/index.html), which is a face recognition API, to use in the front end of the application. This API makes use of the tensorflow library to detect face, and facial expression.

### Face recognition in Front end
- The front end of the application uses the face recognition API to detect the face of the user.
- This method reduces the load on the server as it does not need to detect the face every time the user makes a submission.
- All the work is done in the **client-side** and only the emotion is handled by the server. This method is 


## Framework?
- I have used django as the backend for this project.
- It is HIGH-LEVEL Python web framework.
- It provides blazzingly fast and easy to use web application development.
- This speed and performance allows for developing scalable apps in record time.


## How to setup?

### First make sure, Python 3.8.10 is installed on your system

- The [link](https://www.python.org/downloads/release/python-3810/) to download and install the requied version.

### Clone the repository and start a virtual environment
- Enter in to the repository directory and run the command to create a virtual environment.
- [Pipenv](https://pipenv.pypa.io/en/latest/) is used in this case to setup a fast dev env.

### Install the required packages
- Simple run the below command and move inside the project using `cd`:
```c
pipenv shell
pipenv install
cd engage
```

### [Optional] Load the data in the database
Simply run the implemented command:
```
python manage.py add_data
```
This will load all the movies data if not already present.

### Let us fire up the server!
- This will start our server on the port 8000. Please make sure there are not any other apps running on the port number. If so, can change it with a flag.
```
python manage.py runserver
```

Visit the link: [https://127.0.0.1:8000](https://127.0.0.1:8000) and you will be presented with the login screen :)

