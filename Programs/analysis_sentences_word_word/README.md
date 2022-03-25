### Analyzer of the given text
The output of this program is the percentage of the conversation that is considered to be equivalent to the given category. By default, the program includes two categories, small talk and instructions. The data bases would be created using the most common words and considering the of word before or after it.

If you want to analyze a text with the default program, simply run the program text_analysier.py and answer no to every question in the terminal.

### Creation of both databases:
Small talk: Texts that are used to learn German. Typical text of "how is the weather", "what are you working on" and other topics that serve to "create small talk". Instructions: In this context refers to physiotherapeutic instructions. Texts from physiotherapeutic journals have been used for this purpose. In both cases, an extraction of the most relevant words and the words before or after that will be used for the analysis of the text is made.

### Creation of new categories.
If you want to create a new category, you must go to the text_analysier.py file and add after the imports the following

new_cathegory = an.analyzing_text('new_cathegory ')

To see the result, add a line at the end of the file as follows

print (f'The amount of your text which is new_cathegory is : {percent_words(daten_cleaned,new_cathegory )*100} %' )

When you run the program, answer the questions yes when adding or changing any data base.

Enjoy!
