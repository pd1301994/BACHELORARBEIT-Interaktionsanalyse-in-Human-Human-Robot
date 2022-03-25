import logic.cleaning_data as cl

def analyzing_sentences (text):
    original_file = f'datadirect/{text}.txt'
    text_reader = open(original_file, 'r', encoding='UTF-8')
    data = text_reader.readlines()
    worked_data = []
    y_no = input(f'Are you changing or adding new data in {text}?')
    return_Data = f'datadirect/{text}_extracted_sentences.txt'
    if y_no == 'y':
        with open(return_Data, 'w', encoding='UTF-8') as f:
            data = cl.cleaningdata(data)
            for elements in data:
                f.writelines(f'{elements}\n')
        with open(return_Data, 'r', encoding='UTF-8') as f:
            worked_data_raw = f.readlines()
    else:
        with open(return_Data, 'r', encoding='UTF-8') as f:
            worked_data_raw = f.readlines()
    for lines in worked_data_raw:
        worked_data.append(lines.strip('\n'))
    return worked_data