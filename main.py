from flask import Flask, jsonify, request
import pandas as pd 
import numpy as np
import tensorflow as tf
import io
from PIL import Image
import sqlalchemy


from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

app = Flask(__name__)

emotion_labels = {0: "Happy", 1: "Neutral", 2: "Sad"}
mental_health_labels = {0: "No need for professional help", 1: "Need Professional Help"}


connection = "fabled-variety-351411:us-central1:cloud-sql-instance-2"
db = "my_db"
user = "root"
password = "mindjoy"

pool = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL.create(
        drivername="mysql+pymysql",
        username=user,  
        password=password,  
        database=db,
        query=dict({"unix_socket": "/cloudsql/{}".format(connection)})
    ),
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,
    pool_recycle=1800
)



def predictMentalHealth(data):
    # load model
    model = load_model("mental-health-03.h5")

    predictions = model.predict(data)
    # score = np.where(predictions < 0.5, 0, 1)
    if predictions < 0.5:
        value = "Tidak Butuh Penanganan"
    else:
        value = "Butuh Penanganan"
    return value, int(predictions)


# def processEmotion(IMG_PATH):
#     # load model
#     model = load_model("emotion_classification_01.h5")

#     img = image.load_img(IMG_PATH, target_size=(150, 150))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     images = np.vstack([x])
#     # because on train and test image is normalized, on image predict supposed to be too.
#     images /= 255
#     # the value is not always 1 and 0 because of probabilities
#     classes = model.predict(images, 64)
#     # use to check prediction that have higher probabilities
#     predicted_class_indices = np.argmax(classes)
#     value = "empty"
#     if predicted_class_indices == 0:
#         value = 'Happy'
#     elif predicted_class_indices == 1:
#         value = 'Neutral'
#     else:
#         value = 'Sad'
#     return value

def processEmotion(img):
    # load model
    model = load_model("emotion_classification_01.h5")

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = tf.image.resize(x, [48, 48])
    images = np.vstack([x])
    # because on train and test image is normalized, on image predict supposed to be too.
    images /= 255
    # the value is not always 1 and 0 because of probabilities
    classes = model.predict(images, 64)
    # use to check prediction that have higher probabilities
    predicted_class_indices = np.argmax(classes)
    value = "empty"
    if predicted_class_indices == 0:
        value = 'Happy'
    elif predicted_class_indices == 1:
        value = 'Neutral'
    else:
        value = 'Sad'
    return value


@app.route("/")
def main():
    return "Application is working"


@app.route("/mentalhealth", methods=["POST", "GET"])
def mentalhHealthReq():

    items = ['Gender', 'Are you above 30 years of age?', 'How are you feeling today?',
             'Is your sadness momentarily or has it been constant for a long time?',
             'At what time of the day are you extremely low?',
             'How frequently have you had little pleasure or interest in the activities you usually enjoy?',
             'How confident you have been feeling in your capabilities recently.',
             'Describe how ‘supported’ you feel by others around you – your friends, family, or otherwise.',
             'How frequently have you been doing things that mean something to you or your life?',
             'How easy is it for you to take medical leave for a mental health condition?',
             'How often do you make use of substance abuse(e.g. smoking, alcohol)?',
             'How many hours do you spend per day on watching mobile phone, laptop, computer, television, etc.?',
             'If sad, how likely are you to take an appointment with a psychologist or a counsellor for your current mental state?',
             'How often do you get offended or angry or start crying ?',
             'How likely do you feel yourself vulnerable or lonely?',
             'How comfortable are you in talking about your mental health?']

    # for item in items:
    #     if item not in request.form:
    #         msg = item + " is empty"
    #         return jsonify({"error": msg})
    


    datajsn = request.get_json()
    

    gender = int(datajsn['gender'])
    age = int(datajsn['age'])
    feeling = int(datajsn['feeling'])
    sadness = int(datajsn['sadness'])
    time = int(datajsn['time'])
    interest = int(datajsn['interest'])
    confident = int(datajsn['confident'])
    supported = int(datajsn['supported'])
    things = int(datajsn['things'])
    medical = int(datajsn['medical'])
    substance = int(datajsn['substance'])
    hours = int(datajsn['hours'])
    appointment = int(datajsn['appointment'])
    offended = int(datajsn['offended'])
    vulnerable = int(datajsn['vulnerable'])
    comfortable = int(datajsn['comfortable'])


    
    

    # gender = 1
    # age = 1
    # # age = (age - 1) / (96 - 1)
    # feeling = 1
    # sadness = 1
    # time = 1
    # activities_interest =1
    # confident = 1
    # supported = 1
    # doing_thing = 1
    # medical = 1
    # substance_abuse = 1
    # using_gadget = 1
    # appoinment = 1
    # get_offended = 1
    # vulnerable_lonely =1
    # comfort = 1

    #     data_dummy = [age, "female" if gender == "male" else "female",
    #                   0 if feeling == 1 else 1,
    #                   0 if sadness == 1 else 1,
    #                   0 if feeling == 1 else 1,
    #                   0 if activities_interest == 1 else 1,
    #                   0 if confident == 1 else 1,
    #                   0 if supported == 1 else 1,
    #                   0 if doing_thing == 1 else 1,
    #                   0 if medical == 1 else 1,
    #                   0 if substance_abuse == 1 else 1,
    #                   0 if using_gadget == 1 else 1,
    #                   0 if appoinment == 1 else 1,'
    data_dummy = []

    # gender
    if gender == 0:
        data_dummy.append(0)
    elif gender == 1:
        data_dummy.append(1)
    elif gender == 2:
        data_dummy.append(2)
    else:
        return jsonify({"gender error": "Not Available"})
    # age
    if age == 0:
        data_dummy.append(0)
    elif age == 1:
        data_dummy.append(1)
    else:
        return jsonify({"age error": "Not Available"})
    # feeling
    if feeling == 0:
        data_dummy.append(0)
    elif feeling == 1:
        data_dummy.append(1)
    elif feeling == 2:
        data_dummy.append(2)
    elif feeling == 3:
        data_dummy.append(3)
    else:
        return jsonify({"feeling error": "Not Available"})
    # sadness
    if sadness == 0:
        data_dummy.append(0)
    elif sadness == 1:
        data_dummy.append(1)
    elif sadness == 2:
        data_dummy.append(2)
    elif sadness == 3:
        data_dummy.append(3)
    else:
        return jsonify({"sadness error": "Not Available"})
    # time
    if time == 0:
        data_dummy.append(0)
    elif time == 1:
        data_dummy.append(1)
    elif time == 2:
        data_dummy.append(2)
    else:
        return jsonify({"time error": "Not Available"})
    # activities_interest
    if interest == 0:
        data_dummy.append(0)
    elif interest == 1:
        data_dummy.append(1)
    elif interest == 2:
        data_dummy.append(2)
    elif interest == 3:
        data_dummy.append(3)
    else:
        return jsonify({"interest error": "Not Available"})
    # confident
    if confident == 1:
        data_dummy.append(1)
    elif confident == 2:
        data_dummy.append(2)
    elif confident == 3:
        data_dummy.append(3)
    elif confident == 4:
        data_dummy.append(4)
    elif confident == 5:
        data_dummy.append(5)
    else:
        return jsonify({"confident error": "Not Available"})
    # supported
    if supported == 0:
        data_dummy.append(0)
    elif supported == 1:
        data_dummy.append(1)
    elif supported == 2:
        data_dummy.append(2)
    elif supported == 3:
        data_dummy.append(3)
    else:
        return jsonify({"supported error": "Not Available"})
    # doing_thing
    if things == 0:
        data_dummy.append(0)
    elif things == 1:
        data_dummy.append(1)
    elif things == 2:
        data_dummy.append(2)
    elif things == 3:
        data_dummy.append(3)
    else:
        return jsonify({"things error": "Not Available"})
    # medical
    if medical == 0:
        data_dummy.append(0)
    elif medical == 1:
        data_dummy.append(1)
    elif medical == 2:
        data_dummy.append(2)
    elif medical == 3:
        data_dummy.append(3)
    else:
        return jsonify({"medical error": "Not Available"})
    # substance_abuse
    if substance == 0:
        data_dummy.append(0)
    elif substance == 1:
        data_dummy.append(1)
    elif substance == 2:
        data_dummy.append(2)
    elif substance == 3:
        data_dummy.append(3)
    else:
        return jsonify({"substance error": "Not Available"})
    # using_gadget
    if hours == 0:
        data_dummy.append(0)
    elif hours == 1:
        data_dummy.append(1)
    elif hours == 2:
        data_dummy.append(2)
    elif hours == 3:
        data_dummy.append(3)
    else:
        return jsonify({"hours error": "Not Available"})
    # appointment
    if appointment == 1:
        data_dummy.append(1)
    elif appointment == 2:
        data_dummy.append(2)
    elif appointment == 3:
        data_dummy.append(3)
    elif appointment == 4:
        data_dummy.append(4)
    elif appointment == 5:
        data_dummy.append(5)
    else:
        return jsonify({"appointment error": "Not Available"})
    # offended
    if offended == 0:
        data_dummy.append(0)
    elif offended == 1:
        data_dummy.append(1)
    elif offended == 2:
        data_dummy.append(2)
    elif offended == 3:
        data_dummy.append(3)
    else:
        return jsonify({"offended error": "Not Available"})
    # vulnerable
    if vulnerable == 1:
        data_dummy.append(1)
    elif vulnerable == 2:
        data_dummy.append(2)
    elif vulnerable == 3:
        data_dummy.append(3)
    elif vulnerable == 4:
        data_dummy.append(4)
    elif vulnerable == 5:
        data_dummy.append(5)
    else:
        return jsonify({"vulnerable error": "Not Available"})
    # comfortable
    if comfortable == 1:
        data_dummy.append(1)
    elif comfortable == 2:
        data_dummy.append(2)
    elif comfortable == 3:
        data_dummy.append(3)
    elif comfortable == 4:
        data_dummy.append(4)
    elif comfortable == 5:
        data_dummy.append(5)
    else:
        return jsonify({"comfortable error": "Not Available"})

    data = [data_dummy]
    # data = [[age, gender, feeling, sadness, time, activities_interest, confident, supported, doing_thing, medical,
    #          substance_abuse, using_gadget, appoinment, get_offended, vulnerable_lonely, comfort], data_dummy]

    print(data)
    # data_df = pd.DataFrame(data=data, columns=items)

    # features_cat = pd.get_dummies(data_df[items].astype('category'))
    # features = pd.concat([data_df, features_cat], axis=1)
    # features = features.drop(columns=items).loc[[0], :]
    # print(features)
    resp, predictions = predictMentalHealth(data)
    
    return jsonify({"result": resp, "score": predictions})


@app.route("/emotion", methods=["POST", 'GET'])
def emotionReq():
    if request.method == "POST":
        img = request.files.get("img")
        if img is None:
            return jsonify({"error": "Image is empty"})

        img_bytes = img.read()
        img_final = Image.open(io.BytesIO(img_bytes))

        resp = processEmotion(img_final)

        return jsonify({"result": resp})



@app.route("/register", methods=["POST", "GET"])
def register(): 
    table = "account"

    data_user = request.get_json()

    if data_user:
        querysql = sqlalchemy.text("INSERT INTO {} (name, username, password) VALUES ('{}', '{}', '{}')".format(table, data_user['name'], data_user['username'], data_user['password']))
    else:
        return jsonify({"message": "Register Failed"})
    
    try:
        with pool.connect() as con:
            con.execute(querysql)
            return jsonify({"message": "Register Successful"})
    except Exception as e:
        return jsonify({"message": str(e)})

@app.route("/login", methods=["POST", "GET"])
def login(): 
    table = "account"

    data_user = request.get_json()

    if data_user:
        querysql = sqlalchemy.text("SELECT * FROM {} WHERE username = '{}' and password = '{}'".format(table, data_user['username'], data_user['password']))
    else:
        return jsonify({"message": "Login Failed"})
    
    try:
        with pool.connect() as con:
            res = con.execute(querysql).fetchall()
            if len(res) > 0:
                 return jsonify({"message": "Login Sukses"})
            else:
                 return jsonify({"message": "Login Failed"})
    except Exception as e:
        return jsonify({"message": str(e)})
            


if __name__ == '__main__':
    app.run(debug=True)
