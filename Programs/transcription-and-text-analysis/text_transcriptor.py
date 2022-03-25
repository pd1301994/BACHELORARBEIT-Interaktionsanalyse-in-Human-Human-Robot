import os
import moviepy.editor as mp
from pydub import AudioSegment
import math
from pathlib import Path
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'listdir')
if not os.path.exists(final_directory):
   os.makedirs(final_directory)
#here if you want to change the video
my_clip = mp.VideoFileClip(r"Bizepssehnenentzündung_ 3 sehr effektive Übungen zur Selbstbehandlung (für zuhause).mp4")
my_clip.audio.write_audiofile(r"listdir/my_result.wav")
# code from: https://towardsdatascience.com/extracting-audio-from-video-using-python-58856a940fd



# this code was found in https://www.geeksforgeeks.org/how-to-get-file-size-in-python/
# open file
Path(r'listdir/my_result.wav').stat()
# getting file size
file = Path(r'listdir/my_result.wav').stat().st_size

# display the size of the file
print("Size of file is :", file, "bytes")
# code for splitting wav files in audios:
class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename
        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 10 * 1000
        t2 = to_min * 10 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")

    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 10)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i + min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')


file = 'my_result.wav'
folder = 'listdir'
split_wav = SplitWavAudioMubin(folder, file)
split_wav.multiple_split(min_per_split=1)


from os import listdir

import speech_recognition as sr
r = sr.Recognizer()
for i in range(0, len(listdir('listdir'))):
    file = f"{i}_my_result.wav"
    print(f"From second {(i-1)*10} to second {i*10} text has been transcribed")
    if file in listdir('listdir') and i >= 0:
        audio = sr.AudioFile('listdir/' + file)
        with audio as source:
            audio = r.record(source)
            with open('video_recognizer.txt', 'a', encoding='UTF-8') as f:
                try:

                    f.writelines(f"{r.recognize_google(audio, language='de-DE')}\n")


                except:
                    print("Error in iteration:  " + str(i))
dir = 'listdir'
for i in os.listdir(dir):
    os.remove(os.path.join(dir, i))
    print (f" removing files:  {i}")


