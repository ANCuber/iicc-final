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
#### package
```
pip install --upgrade pip // Can be skipped if already did before
pip install audio-similarity==1.0.0
```
#### file conversion
##### On Mac
```
brew install ffmpeg
```
##### On Linux
```
sudo apt install ffmpeg
```
Now the environment should be ready.

### Run the Code
#### Convert .m4a to .wav
Firstly, you need to move the target audio file to `soundtrack` directory from your iPhone, and rename it `test-X.m4a`, where X is the index of the problem. Afterwards, run the following command.
```
ffmpeg -i test-X.m4a test-X.wav
```
#### Run main.py
Run the following command.
```
python main.py
```




