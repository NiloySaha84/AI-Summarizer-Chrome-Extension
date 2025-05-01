import speech_recognition as sr
from flask import flash
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


def yt_audioExtractor(videoLink):
    video_id = parse_qs(urlparse(videoLink).query).get("v", [None])[0]
    if not video_id:
        raise ValueError("Could not extract video ID from URL")

    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'en-US', 'en-GB'])
        transcript = "\n".join([entry["text"] for entry in transcript_data])
        return transcript
    except Exception as e:
        raise RuntimeError("Captions not available or language couldn't be understood") from e



def preprocess(videoLink=None):

    yt_audio = yt_audioExtractor(videoLink=videoLink)
    if yt_audio:
        return yt_audio
    else:
        flash("Audio Transcription not found", "error")
        return "Audio Transcription not found"

        

def transcribe_audio(audio_path):
    r = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            r.adjust_for_ambient_noise(source)
            raw_audio = r.record(source)
        transcribed_audio = r.recognize_google(raw_audio)
        return transcribed_audio
    except sr.UnknownValueError:
        return "Google Web Speech API could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Web Speech API; {e}"

