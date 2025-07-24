import streamlit as st
from audio_similarity import AudioSimilarity
from pydub import AudioSegment
import os
import tempfile

st.title("Sound Effect Similarity Checker")

# Let user pick reference sound ID
testcase = st.text_input("Enter Problem ID (e.g. 1, 2, 3):")

# Let user upload an m4a file
uploaded_file = st.file_uploader("Upload your mock .m4a file", type=["m4a"])

if uploaded_file and testcase:
    try:
        # Read and convert uploaded file to .wav using a temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".m4a") as temp_m4a:
            temp_m4a.write(uploaded_file.read())
            temp_m4a.flush()
            audio = AudioSegment.from_file(temp_m4a.name, format="m4a")

        # Export to wav
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav:
            compare_path = temp_wav.name
            audio.export(compare_path, format="wav")

        original_path = "answers"
        sample_rate = 44100
        weights = {
            'zcr_similarity': 0.00,
            'rhythm_similarity': 0.00,
            'chroma_similarity': 0.00,
            'energy_envelope_similarity': 0.50,
            'spectral_contrast_similarity': 0.50,
            'perceptual_similarity': 0.00
        }

        st.info("Calculating similarity...")

        audio_similarity = AudioSimilarity(
            original_path=original_path,
            compare_path=compare_path,
            sample_rate=sample_rate,
            weights=weights,
            verbose=False
        )

        similarity_score = audio_similarity.stent_weighted_audio_similarity(metrics='all')
        result = similarity_score['swass'] * 100

        st.success(f"Similarity Score: **{result:.2f}%**")

    except Exception as e:
        st.error(f"Something went wrong: {str(e)}")

elif uploaded_file and not testcase:
    st.warning("Please enter a valid problem ID.")


