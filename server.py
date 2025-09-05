'''
This is the entrypoint of the Flask app
'''
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotions():
    '''
    This function is a route handler used to detect and return emotions
    from the given user input as well as which one is the most dominant
    '''
    text_to_analyze = request.args.get('textToAnalyze', '')
    result:dict = emotion_detector(text_to_analyze)
    dominant_emotion = result.get('dominant_emotion')
    if not dominant_emotion:
        return "Invalid text! Please try again!"
    anger = result.get('anger', '')
    disgust = result.get('disgust', '')
    fear = result.get('fear', '')
    joy = result.get('joy', '')
    sadness = result.get('sadness', '')
    return f"For the given statement, the system response is 'anger': {anger}," \
    + f" 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}." \
    + f" The dominant emotion is {dominant_emotion}."

@app.route("/")
def home():
    '''
    Displays home page
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
