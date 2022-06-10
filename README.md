# MINDJOY-CC
### API DOCUMENTATION REVISION
This is the documentation for our revision API. We're doing this revision because there's a technical issue with deploying the API and the model; to save on the cost of using the Google cloud platform because we have less credit and we want to re-deploying them again, we combine the API that we previously wrote with javascript and then convert it into python to a machine learning model so that it can be processed at once, saving us money over having to process them individually.

### Deploy Backend Register
- URL : `https://mindjoy-cc-avpq3ri45q-as.a.run.app`
- endpoint : /register
- parameter : (username,name,password)
### Deploy Backend Login
- URL : `https://mindjoy-cc-avpq3ri45q-as.a.run.app`
- endpoint : `/login`
- parameter : (username,password)
### Deploy Backend Image Expression (Machine Learning Model)
- URL : `https://mindjoy-cc-avpq3ri45q-as.a.run.app`
- endpoint : `/emotion`
- parameter :
   (gender,
    age, 
    feeling,
    sadness,
    time,
    activities_interest,
    confident,
    supported,
    doing_thing,
    medical,
    substance_abuse,
    using_gadget,
    appoinment,
    get_offended,
    vulnerable_lonely,
    comfort)
#### We use APP Engine and Cloud SQL for deploying API. Here is the following workflow:
1. Make a database for registration and quiz data in Cloud SQL.
2. Connecting API in Visual Code Studio to CLoud SQL, we use IP address, databases name, and the same password in Cloud SQL.
3. Connecting APP Engine to Cloud SQL.

### Deploy Machine Learning Model

URL Deploy Image:
https://getprediction-avpq3ri45q-as.a.run.app
<br />
URL Deploy Quiz:
https://getresultquiz-avpq3ri45q-as.a.run.app
<br />
#### We use Cloud Run and Cloud SDK for deploying Machine Learning Model. Here is the following workflow:
1. Prepare model.
2. Download and install Google Cloud SDK
3. Make a Dockerfile.
4. Deploying the model using this code:

* Deploying Image Model
1. gcloud builds submit --tag gcr.io/fabled-variety-351411/emotionreq
2. gcloud run deploy --image gcr.io/fabled-variety-351411/emotionreq --platform managed

* Deploying Quiz Model
1. gcloud builds submit --tag gcr.io/fabled-variety-351411/mentalhealthreq
2. gcloud run deploy  gcr.io/fabled-variety-351411/mentalhealthreq --image platform managed
