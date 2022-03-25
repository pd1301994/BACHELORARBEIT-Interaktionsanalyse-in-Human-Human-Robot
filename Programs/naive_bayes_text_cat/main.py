import converting_sents as s

file = open('video_recognizer.txt', 'r', encoding='UTF-8')

data = file.readlines()
sml = 0
inst = 0
count = 0
for lines in data:
    if s.sentiment(lines)[0] == 'sml':
        sml = sml + 1
    if s.sentiment(lines)[0] == 'ins':
        inst = inst + 1
    count = count + 1
print(f"percentage of small talk is = {sml / count * 100} ")
print(f"percentage of instruction  talk is = {inst / count * 100} ")
