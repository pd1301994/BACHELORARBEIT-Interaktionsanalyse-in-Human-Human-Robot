import nltk
from HanTa import HanoverTagger as ht
def cleaningdata(data):
    tagger = ht.HanoverTagger('morphmodel_ger.pgz')
    words_appear = []
    for lines in data:
        lines = lines.lower()
        tokenized_sent = nltk.tokenize.word_tokenize(lines, language='german')

        for i in range(0, len(tokenized_sent)):
            try:

                if tagger.analyze(tokenized_sent[i])[1] == 'VAFIN' or tagger.analyze(tokenized_sent[i])[
                    1] == 'ADV' or tagger.analyze(tokenized_sent[i])[1] == 'NN' or tagger.analyze(tokenized_sent[i])[1] == 'VVFIN'\
                       or  tagger.analyze(tokenized_sent[i])[1] == 'VMFIN' or  tagger.analyze(tokenized_sent[i])[1] == 'VMINF'\
                        or tagger.analyze(tokenized_sent[i])[1] ==  'VVPP':


                    words_appear.append([tagger.analyze(tokenized_sent[i - 1])[1],
                                         tagger.analyze(tokenized_sent[i])[0]])
                    words_appear.append([tagger.analyze(tokenized_sent[i])[0],
                                         tagger.analyze(tokenized_sent[i + 1])[1]])


            except:
                continue
    return words_appear


