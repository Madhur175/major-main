from flask import jsonify
from app.models import AudioSentiment
from app.utils import transcribe_file, analyze_sentiment
import os

def get_audio_sentiments_controller():
    audio_folder_path = "audio_files"
    batch_size = 2  # Set the batch size

    if not os.path.exists(audio_folder_path):
        return jsonify({"error": "Audio folder not found"}), 404

    audio_files = os.listdir(audio_folder_path)

    # Get existing sentiments from the database
    existing_sentiments = {record[0]: record[1] for record in AudioSentiment().get_sentiments()}

    # Process and store sentiments for audio files
    audio_sentiments = {}

    for audio_file in audio_files:
        if audio_file not in existing_sentiments:
            # Process sentiment for new audio file
            transcript = transcribe_file(os.path.join(audio_folder_path, audio_file))
            sentiment = analyze_sentiment(transcript)
            
            # Store sentiment in the database
            AudioSentiment().add_sentiment(audio_file, sentiment)
        else:
            # Use sentiment from the database
            sentiment = existing_sentiments[audio_file]

        # Add sentiment to the response
        audio_sentiments[audio_file] = sentiment

    return jsonify(audio_sentiments)
