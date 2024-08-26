import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, json=input_json)

    if not text_to_analyze:
        response.status_code = 400
    
    if response.status_code == 200:
        response_json = response.json()
        emotions = response_json['emotionPredictions'][0]['emotion']
        
        # Extracting the required emotions
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)
        
        # Finding the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Formatting the output
        formatted_output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
        return formatted_output
    elif response.status_code == 400:
        formatted_output = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return formatted_output
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage
if __name__ == "__main__":
    text_to_analyze = "I love"
    result = emotion_detector(text_to_analyze)
    print(result)