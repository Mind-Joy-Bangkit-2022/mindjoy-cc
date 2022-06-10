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

