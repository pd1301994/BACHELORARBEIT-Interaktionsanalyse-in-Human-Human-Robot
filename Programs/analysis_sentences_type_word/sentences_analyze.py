import logic.cleaning_data as cl
import logic.extractig_words as an

small_text = an.analyzing_sentences('smalltalk')
instr_text  = an.analyzing_sentences('instructions')
daten_cleaned = []


with open('video_recognizer.txt', 'r', encoding='UTF-8') as f:
    daten = f.readlines()
    daten = cl.cleaningdata(daten)
    for value in daten:
        daten_cleaned.append(str(value))


def percent_words (clean_data,pattern):
    sum_factors = 0
    for words in clean_data:
        if words in pattern:
            sum_factors = sum_factors+1
    return sum_factors/len(clean_data)



print (f'The amount of your text which is Small conversation is : {percent_words(daten_cleaned,small_text)*100 } %' )
print (f'The amount of your text which is instructions is :  {percent_words(daten_cleaned,instr_text)*100} %' )


