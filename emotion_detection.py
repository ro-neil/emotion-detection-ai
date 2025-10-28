"""
Emotion Detection Module
"""

import requests, json

def emotion_detector(text_to_analyse):
    """
    This function analyzes text using Watson AI and returns
    a JSON string conaining scores associated with each related emotion
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    json_input = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = json_input, headers=header)
    json_response = json.loads(response.text)
    emotionPredictions = json_response['emotionPredictions']
    emotions = emotionPredictions[0]['emotion']
    dominant_emotion = {
        'emotion': '',
        'score': 0
    }
    for emotion, score in emotions.items():
        if score > dominant_emotion['score']:
            dominant_emotion['emotion'] = emotion
            dominant_emotion['score'] = score
    emotions['dominant_emotion'] = dominant_emotion['emotion']
    return emotions
