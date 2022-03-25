import nltk
from nltk.corpus import stopwords
from HanTa import HanoverTagger as ht
def cleaningdata(datos):

    tagger = ht.HanoverTagger('morphmodel_ger.pgz')
    stop_words = stopwords.words('german')
    words_appear = []
    for lines in datos:
        lines = lines.lower()

        tokenized_sent = nltk.tokenize.word_tokenize(lines, language='german')
        tokens_without_sw = [lines for lines in tokenized_sent if not lines in stop_words]
        for words in tokens_without_sw:
            try:
                if tagger.analyze(words)[1] == 'VVINF' or tagger.analyze(words)[1] == 'ADV' or tagger.analyze(words)[
                    1] == 'NN' or \
                        tagger.analyze(words)[1] == 'VVFIN' or tagger.analyze(words)[1] == 'VMFIN' or tagger.analyze(words)[1] == 'VMINF' or tagger.analyze(words)[1] == 'VVPP':
                    words_appear.append(tagger.analyze(words))

            except:
                print("nothing found here")
    return words_appear

