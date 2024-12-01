import requests, json
from flask import jsonify, Flask, request, render_template, url_for

FLASK_APP = "app.py"
FLASK_ENV = "development"

app=Flask("Emotion_Detection")
 
@app.route("/detect_emotion",methods=["POST"])
def emotion_detector():
    req_json = request.get_json()
    text_to_analyze: str = ""
    if req_json["to_analyse"]:
        text_to_analyze = req_json["to_analyse"]
    
    watson_url: str = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_to_send = {"raw_document": {"text":text_to_analyze}}
    #json_to_send = json.dumps(json_to_send)
    print("*****")
    print(json_to_send)
    print("*****")
    # URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Input json: { "raw_document": { "text": text_to_analyse } }
    to_return = requests.put(watson_url, headers=header, json=json_to_send)
    
    #to_return = ""
    print(to_return)
    return to_return


#print(emotion_detector("Interesantísima oferta de Carrefour. Si compras la botella de 3 litros, el aceite de oliva virgen extra te sale un 21% más caro que si te llevas la de 1 litro."))

if __name__=="__main__":
    app.run(debug=True)