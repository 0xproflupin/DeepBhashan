
import librosa
import soundfile as sf
from pathlib import Path
import os

abc = os.listdir('C:\\Users\\Deepankar\\Desktop\\sru\\validate')
i=0
for entry in abc:
    print(entry)
    x,_ = librosa.load('C:\\Users\\Deepankar\\Desktop\\sru\\validate\\'+str(entry),sr=16000)
    sf.write(entry, x, 16000)
    print(i)
    i+=1
