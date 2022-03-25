
import logic.cleaning_data as cl
import logic.text_analizer as an



small_text = an.analyzing_text('smalltalk')
instr_text  = an.analyzing_text('instructions')
daten_cleaned = []


with open('video_recognizer.txt', 'r', encoding='UTF-8') as f:
    daten = cl.cleaningdata([word for line in f for word in line.split()])
    for value in daten:
        daten_cleaned.append(value[0])


def percent_words (clean_data,pattern):
    sum_factors = 0
    for words in clean_data:
        if words in pattern:
            sum_factors = sum_factors+1
    return sum_factors/len(clean_data)



print (f'The amount of your text which is Small conversation is : {percent_words(daten_cleaned,small_text)*100 } %' )
print (f'The amount of your text which is instructions is :  {percent_words(daten_cleaned,instr_text)*100} %' )



