import torch
import os
import whisper
from pyannote.audio import Pipeline, Audio

file = input("Enter the path to the wav file: ")
speaker_num = int(input("Enter the number of speakers: "))

model = whisper.load_model("large")

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token=os.environ["HUGGINGFACE_ACCESS_TOKEN"])
# send pipeline to GPU (when available)
pipeline.to(torch.device("mps"))

diarization = pipeline(file, num_speakers=speaker_num)
audio = Audio(sample_rate=16000, mono=True)

for segment, _, speaker in diarization.itertracks(yield_label=True):
    waveform, sample_rate = audio.crop(file, segment)
    text = model.transcribe(waveform.squeeze().numpy())["text"]
    print(f"[{segment.start:03.1f}s - {segment.end:03.1f}s] {speaker}: {text}")
