# MINDJOY-CC
### API DOCUMENTATION REVISION
This is the documentation for our revision API. We're doing this revision because there's a technical issue with deploying the API and the model; to save on the cost of using the Google cloud platform because we have less credit and we want to re-deploying them again, we combine the API that we previously wrote with javascript and then convert it into python to a machine learning model so that it can be processed at once, saving us money over having to process them individually.

### Deploy Backend Register
- URL : `https://mindjoy-cc-avpq3ri45q-as.a.run.app`
- endpoint : `/register`
- parameter : (username,name,password)
### Deploy Backend Login
- URL : `https://mindjoy-cc-avpq3ri45q-as.a.run.app`
- endpoint : `/login`
- parameter : (username,password)
### Deploy Model Quiz (Machine Learning Model)
- URL : `https://mindjoy-cc-avpq3ri45q-as.a.run.app`
- endpoint : `/mentalhealth`
- parameter :
    {"gender" : 1,
    "age" : 1,
    "feeling" : 2,
    "sadness" : 2,
    "time" : 2,
    "interest" : 2,
    "confident" : 3,
    "supported" : 3,
    "things" : 2,
    "medical" : 3,
    "substance" : 3,
    "hours" : 1,
    "appointment" : 1,
    "offended" : 1,
    "vulnerable" : 1,
    "comfortable" : 1} <br/> The parameter values is integer/number.

### Deploy Model Image Expression (Machine Learning Model)
- URL : `https://mindjoy-cc-avpq3ri45q-as.a.run.app`
- endpoint : `/emotion`
- parameter : image -> file

### LANDING PAGE DOCUMENTATION
![home Page - ](https://user-images.githubusercontent.com/79590008/173270381-7626f3f6-dae2-4994-90bd-da9857045e39.png)
![ss fitur 1](https://user-images.githubusercontent.com/79590008/173270514-6f553b50-1c29-4fdd-ab3a-cfa116b85541.png)
![ss fitur 2](https://user-images.githubusercontent.com/79590008/173270555-522da21d-ed5f-4ef9-a0d0-a9cdf895f55e.png)
![step part](https://user-images.githubusercontent.com/![tim 1](https://user-images.githubusercontent.com/79590008/173270599-1f1c17fb-4a34-4b70-80bb-a2ba65b1626d.png)!
![tim 1](https://user-images.githubusercontent.com/79590008/173270634-dff47945-7b79-4db7-af6d-4de1bf36f7d6.png)
![tim 2](https://user-images.githubusercontent.com/79590008/173270657-d2e0e1ba-0bbb-4582-b793-df49047bc5cc.png)
![hope 1](https://user-images.githubusercontent.com/79590008/173270739-1edada56-d4b9-4173-ab47-706f9b9d6a83.png)
![hope 2](https://user-images.githubusercontent.com/79590008/173270769-633a9e27-4623-4f0a-9aeb-349ab3c9b862.png)
![last](https://user-images.githubusercontent.com/79590008/173270808-7518e757-061e-4613-bcbe-eb6c5eadd4b9.png)



