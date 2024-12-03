import unittest
import requests
import json
from EmotionDetection import emotion_detection

class TestEmotionDetection(unittest.TestCase):
    
    
    def test_emotion_detectior(self):
        test_url: str = "http://127.0.0.1:5000/detect_emotion"

        test1="I am glad this happened"
        test2="I am really mad about this"
        test3="I feel disgusted just hearing about this"
        test4="I am so sad about this"
        test5="I am really afraid that this will happen"
        
        res1=""
        res2=""
        res3=""
        res4=""
        res5=""
        
        exp1="joy"
        exp2="anger"
        exp3="disgust"
        exp4="sadness"
        exp5="fear"
        
        to_analyse = {"to_analyse": test1}
        response = json.loads(requests.post(test_url, json=to_analyse).text)
        res1 = response["dominant_emotion"]
        
        to_analyse = {"to_analyse": test2}
        response = json.loads(requests.post(test_url, json=to_analyse).text)
        res2 = response["dominant_emotion"]

        to_analyse = {"to_analyse": test3}
        response = json.loads(requests.post(test_url, json=to_analyse).text)
        res3 = response["dominant_emotion"]

        to_analyse = {"to_analyse": test4}
        response = json.loads(requests.post(test_url, json=to_analyse).text)
        res4 = response["dominant_emotion"]

        to_analyse = {"to_analyse": test5}
        response = json.loads(requests.post(test_url, json=to_analyse).text)
        res5 = response["dominant_emotion"]

        expected= [exp1,exp2,exp3,exp4,exp5]
        received= [res1,res2,res3,res4,res5]

        #emotion_detection.app.run()
        print(expected)
        print(received)
        self.assertEqual(expected,received)

if __name__ == "__main__":
    unittest.main()
