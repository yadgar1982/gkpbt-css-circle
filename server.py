"""
server.py

Flask application for detecting emotions in user-provided text.
Provides a web interface and an API endpoint to analyze text
and return emotion scores and the dominant emotion.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def render_index_page():
    """
    Render the main index.html page.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template("index.html")


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Analyze the text provided by the user and return emotion scores.

    Args:
        textToAnalyze (str): Text input to analyze emotions.

    Returns:
        str: Formatted result showing emotion scores and dominant emotion.
             If input is blank or invalid, returns an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.get("dominant_emotion")

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response.get("anger")
    disgust = response.get("disgust")
    fear = response.get("fear")
    joy = response.get("joy")
    sadness = response.get("sadness")

    result = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return result


if __name__ == "__main__":
    """
    Run the Flask application on localhost:5000.
    """
    app.run(host="0.0.0.0", port=5000)
