"""Module providing a function printing python version."""

import requests
import json
from flask import Flask, request, render_template
#pylint emotion_detection.py 

FLASK_APP = "app.py"
FLASK_ENV = "development"

app=Flask("Emotion_Detection")

@app.route("/emotionDetector",methods=["POST"])
@app.route("/detect_emotion",methods=["POST","GET"])
def emotion_detector(text_to_analyze:str = ""):
    if request.method == "GET":
        request.args.get("textToAnalyze")
        text_to_analyze = request.args.get("textToAnalyze")
        print(text_to_analyze)
    if request.method == 'POST' or text_to_analyze != "":
        req_json = request.get_json()
        if req_json["to_analyse"]:
            text_to_analyze = req_json["to_analyse"]

    watson_url: str = 'https://sn-watson-emotion.labs.skills.network/'
    watson_url = watson_url + 'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_to_send = {"raw_document": {"text":text_to_analyze}}
    to_return = requests.post(watson_url, headers=header, json=json_to_send)
    print (json_to_send)
    formatted_response = json.loads(to_return.text)
    label = formatted_response['emotionPredictions'][0]["emotion"]
    keys = label.keys()
    max_val = 0
    max_name = ""
    print (keys)
    for key in keys:
        if label[key] > max_val:
            max_val = label[key]
            max_name = key
    label["dominant_emotion"] = max_name
    print (label)
    print(type(label))
    return label

@app.route("/emotionDetector",methods=["get"])
@app.route("/",methods=["GET"])
def index():
    text_to_analyze = request.args.get("textToAnalyze")
    if text_to_analyze:
        test_url: str = "http://127.0.0.1:5000/emotionDetector"
        to_analyse = {"to_analyse": text_to_analyze}
        response = json.loads(requests.post(test_url, json=to_analyse).text)
        return response
    else:
        return render_template("index.html",responseText = text_to_analyze)
    #return "SOME TEXTO"

@app.errorhandler(404)
@app.errorhandler(400)
def errorhandler(e):
    return "Page not found."

if __name__=="__main__":
    app.run(debug=True)
