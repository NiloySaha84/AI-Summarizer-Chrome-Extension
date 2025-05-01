from flask import Blueprint, render_template, request, flash, jsonify, Flask
from .preprocessing import preprocess
from .summarize import summarize

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

views = Blueprint('views', __name__)
@views.route('/', methods=['GET', 'POST'])
def home():
    transcription = ""
    return render_template("home.html", transcription=transcription)

@views.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    text = data.get("text", "")
    url = data.get("url", "")
    if url and "youtube.com/watch" in url or "youtu.be/" in url or "youtube.com/shorts" in url:
        try:
            summary = summarize(text=preprocess(videoLink=url))
            return jsonify({"summary": summary})
        except Exception as e:
            return jsonify({"error": f"Failed to transcribe YouTube video: {e}"}), 500
    elif not text:
        return jsonify({"error": "No text provided"}), 400

    else:
        summary = summarize(text=text)
        return jsonify({"summary": summary})
