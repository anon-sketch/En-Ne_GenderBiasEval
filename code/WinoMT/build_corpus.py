from deep_translator import GoogleTranslator
import pandas as pd
from tqdm import tqdm

with open('en_anti.txt','r') as infile:
    sentences = infile.readlines()

with open('conjunctions.txt','r') as conj_file:
    conjunctions = conj_file.readlines()

first_halves = []
second_halves = []
conjs = []

sentence_details = []

for sentence in tqdm(sentences[130:]):
    sentence_detail = []
    metadata = sentence.strip()
    sentence_detail= metadata.split('\t')
    en_text = metadata.split('\t')[2]

    for conj in conjunctions:
        if f" {conj.strip()} " in en_text:
            halves = en_text.split(f" {conj.strip()} ")
            sentence_detail.append(halves[0])
            sentence_detail.append(GoogleTranslator(source='en', target='ne').translate(halves[0]))
            sentence_detail.append(halves[1])
            sentence_detail.append(GoogleTranslator(source='en', target='ne').translate(halves[1]))
            sentence_detail.append(conj.strip())
            break
    
    sentence_details.append(sentence_detail)

    data_df = pd.DataFrame([sentence_detail])
    data_df.to_csv('ne_anti.csv', mode='a', header=False, index=False)