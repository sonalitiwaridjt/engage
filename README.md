# engage-submission


## How to setup?

### First make sure, Python 3.8.10 is installed on your system

The [link](https://www.python.org/downloads/release/python-3810/) to download and install the requied version.

### Clone the repository and start a virtual environment
Enter in to the repository directory and run the command to create a virtual environment. [Pipenv](https://pipenv.pypa.io/en/latest/) is used in this case to setup a fast dev env.

### Install the required packages
Simple run the below command and move inside the project using `cd`:
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
This will start our server on the port 8000. Please make sure there are not any other apps running on the port number. If so, can change it with a flag.
```
python manage.py runserver
```

Visit the link: [https://127.0.0.1:8000](https://127.0.0.1:8000) and you will be presented with the login screen :)

