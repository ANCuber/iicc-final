# Audio Similarity Comparison

The code here is used for 22-nd iicc final, where we need to compare the similarity of two audio data. The main reference is from [this package](https://pypi.org/project/Audio-Similarity/).

## How to Use?

### Environment
Run the following commands on your (Visual Studio Code) terminal.
#### venv
```
python -m venv venv // Can be skipped if already did before
source venv/bin/activate
```
#### file conversion
##### On Mac
```
brew install ffmpeg
```
Now the environment should be ready.
#### package
```
pip install --upgrade pip // Can be skipped if already did before
pip install audio-similarity==1.0.0 streamlit pydub
```

### Run the Code
Run the following command and follow the instructions in a webpage.
```
streamlit python3 app.py
```




