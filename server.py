from flask import Flask, request, render_template, abort
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotions():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze: abort(400)
    result = emotion_detector(text_to_analyze)
    anger = result.get('anger', '')
    disgust = result.get('disgust', '')
    fear = result.get('fear', '')
    joy = result.get('joy', '')
    sadness = result.get('sadness', '')
    dominant_emotion = result.get('dominant_emotion', '')
    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    
@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)