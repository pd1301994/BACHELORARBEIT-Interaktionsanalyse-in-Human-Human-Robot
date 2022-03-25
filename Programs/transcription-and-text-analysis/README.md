# Transcription and Text analysis: 
This program has been created for academic purposes
#            1st!

````
pip install -r requirements.txt
````
Purpose of the program: 
# 1. Audio transcription with mp4 files
The transcript will be written to a text file named video_recognizer2.txt. To transcribe a video, enter the path in the "my_clip" variable of the text_transcriptor.py file. If you want to do another transcription THIS FILE MUST BE DELETED!!!
Run the file text_transcriptor.py. 
The program transcribes the text file, divides it into 10-second segments and extracts the text from each of the segments (this type of technology only allows to extract 10mb).
The created audio files are stored in a "list_dir" folder that will be created automatically. These audio files will be deleted once all the audio has been transcribed. This way, no space will be taken up on your local machine. 

#  2. Analyser of the given text
The output of this program is the percentage of the conversation that is considered to be equivalent to the given category. 
By default, the program includes two categories, small talk and instructions. A database has been created with the most common words in each category. 
The text will be analyzed according to the occurrence or not of these words. 

If you want to analyze a text with the default program, simply run the program text_analysier.py and answer no to every question in the terminal. 

#   Creation of both databases:
- Small talk: Texts that are used to learn German. Typical text of "how is the weather", "what are you working on" and other topics that serve to "create small talk".
- Instructions: In this context refers to physiotherapeutic instructions. Texts from physiotherapeutic journals have been used for this purpose. 

In both cases, an extraction of the most relevant words that will be used for the analysis of the text is made.
# 3. Creation of new categories. 
If you want to create a new category, you must go to the text_analysier.py file and add after the imports the following

new_cathegory = an.analyzing_text('new_cathegory ')

To see the result, add a line at the end of the file as follows

print (f'The amount of your text which is new_cathegory is : {percent_words(daten_cleaned,new_cathegory )*100} %' )

When you run the program, answer the questions yes when adding or changing any data base. 

Enjoy!
