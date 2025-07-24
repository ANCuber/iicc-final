from audio_similarity import AudioSimilarity
from pydub import AudioSegment
import os

# === CONFIGURATION ===

# Path to your original audio folder (can contain .m4a files)
original_path = 'answers'  # folder with original sound effects

# Path to the file you want to compare against (can also be .m4a)
testcase = str(input("Please enter the ID (a number) of the problem: "))
mock_effect = 'soundtrack/test-'+testcase+'.m4a'

try:
    audio = AudioSegment.from_file(mock_effect, format="m4a")
except:
    print("Invalid problem ID or No file.")
    exit(1)

compare_path = "output-"+testcase+".wav"
audio.export(compare_path, format="wav")


# Sample rate and metric weights (adjust as needed)
sample_rate = 44100
weights = {
    'zcr_similarity': 0.00,
    'rhythm_similarity': 0.00,
    'chroma_similarity': 0.00,
    'energy_envelope_similarity': 0.50,
    'spectral_contrast_similarity': 0.50,
    'perceptual_similarity': 0.00
}

sample_size = None   # Speed optimization for folders with many files
verbose = True     # Print progress

# === RUN COMPARISON ===

# Create the similarity object
audio_similarity = AudioSimilarity(
    original_path=original_path,
    compare_path=compare_path,
    sample_rate=sample_rate,
    weights=weights,
    verbose=verbose,
    sample_size=sample_size
)

# Optional: calculate individual metric
# zcr_score = audio_similarity.zcr_similarity()
# print(f"ZCR Similarity: {zcr_score:.4f}")

# Full similarity score (Stent Weighted Audio Similarity Score - SWASS)
similarity_score = audio_similarity.stent_weighted_audio_similarity(metrics='all')
result = similarity_score['swass'] * 100
print(f"Stent Weighted Audio Similarity: {result:.3f}%")

