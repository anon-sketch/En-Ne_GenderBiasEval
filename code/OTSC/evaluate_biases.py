import nltk

def eval_p_context(data):
    n_w=0
    n_m=0
    n_n=0
    count = 0
    for sentence in data:
        count = count+1
        token = nltk.word_tokenize(sentence.strip().lower())
        if 'her' in token:
            n_w = n_w+1
        elif 'him' in token:
            n_m = n_m+1
        else:
            n_n = n_n+1
    p_w = n_w/count
    p_m = n_m/count
    p_n = n_n/count
    return round(p_m*100,2), round(p_w*100,2), round(p_n*100,2)

translators = ['google','indictrans2','gpt4o']
folders = ['formal','informal']
files = [
    'female_sathi_female.txt',
    'female_sathi_male.txt',
    'male_sathi_female.txt',
    'male_sathi_male.txt'
]

for translator in translators:
    for folder in folders:
        for file in files:
            try:
                print(f"\n\n{translator} {folder} {file}")
                with open(f'en_corpus_from_ne/{translator}/{folder}/{file}', 'r') as input_file:
                    sentences = input_file.readlines()
                    print(eval_p_context(sentences))
            except:
                continue
# listt2 = [female_female, female_male, male_female, male_male]