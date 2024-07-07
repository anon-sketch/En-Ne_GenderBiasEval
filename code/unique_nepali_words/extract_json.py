import json

file = open('dict.json')
data = json.load(file)

with open('nepali_words.txt', 'a') as english_file:
    for data_item in data:
        try:
            if data_item['English'] == 'begger':
                english_file.write(f"{data_item['English']} - {data_item['Nepali'][0]['meanings']}\n")
        except:
            continue