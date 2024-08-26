"""
This module contains the Flask application for the Emotion Detection project.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index.html page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Detect the emotion from the provided text.

    Returns:
        JSON: A JSON response with the emotion analysis result or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again!"
    else:
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        )

    return jsonify(response_text)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
