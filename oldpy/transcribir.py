import whisper

# Load the Whisper model

model = whisper.load_model("turbo")

# Load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("TRINIDAD.mp3")
audio = whisper.pad_or_trim(audio)

# Make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

# Detect the spoken language
_, probs = model.detect_language(mel)
detected_language = max(probs, key=probs.get)
print(f"Detected language: {detected_language}")

# Decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# Define the filename for the output text file
output_filename = "transcription.txt"

# Open the file in write mode ('w') and save the recognized text
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(f"Detected language: {detected_language}\n")
    f.write(result.text)

print(f"The transcription has been saved to '{output_filename}'")