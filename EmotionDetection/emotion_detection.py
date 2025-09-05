import requests, json

def emotion_detector(text_to_analyze:str)->dict:
    url: str ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers:dict = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload: dict = { "raw_document": { "text": text_to_analyze } }
    res = requests.post(url, json=payload, headers=headers)
    status: int = res.status_code
    if status == 400:
        return {key:None for key in ("anger", "disgust", "fear",  
        "joy", "sadness", "dominant_emotion",)}
    res_data: dict = json.loads(res.text)
    emotions: dict = res_data["emotionPredictions"][0]["emotion"]
    emotions['dominant_emotion'] = max(emotions.items(), key=lambda x:x[1])[0]
    return emotions