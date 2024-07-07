import pandas as pd

data_df = pd.read_csv('english_original/ne_anti_improved.csv')

first_halves = data_df['ne_half1'].tolist()
second_halves = data_df['ne_half2'].tolist()
conjs = data_df['nepali_conj'].tolist()
gold_gender_labels = data_df['gender'].tolist()

sentences = []
gold_labels = []
for i, first_half in enumerate(first_halves):
    try:
        first_half = first_half.replace("।","")
        second_half = second_halves[i].replace("।","")

        if first_half != "":
            if conjs[i] in ["तापनि", "कारणले", "की भनेर", "भनेर"]:
                sentence = second_half + " " + conjs[i] + " " + first_half
            else:
                sentence = first_half + " " + conjs[i] + " " + second_half
        sentences.append(sentence)
        gold_labels.append(gold_gender_labels[i])
    except:
        continue

with open('final_corpus/ne_anti.txt', 'w') as outfile:
    for i, sentence in enumerate(sentences):
        outfile.write(f"{sentence}\n")