# Google Cloud Function Course
## Starting a project
To start a new project in google cloud we can go to the [Firebase Console](https://console.firebase.google.com)
or create it from [google cloud platform console](https://console.cloud.google.com).
## Creating a virtual environment
First we have to install `python3 -venv` with the following command:
```
sudo apt install python3-venv
```
Then we excute the following command:
```
python3 -m venv venv
```
To activate the virtual environment we do:
```
source venv/bin/activate
```
In order to add new packages to our virtual environment we create a file called `requirments.txt` and excute the folliwing command:
```
pip install -r requirments.txt
```

## Deploying our functions
First, we have to set our project ID with the following command:
```
gcloud config set project [YOUR_PROJECT_ID]
```
Then we deploy our function with this command:
```
gcloud functions deploy [FUNCTION_NAME] --runtime python37 --trigger-http
```