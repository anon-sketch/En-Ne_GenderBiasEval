import numpy as np
import pandas as pd
import nltk
from tqdm import tqdm


def read_data(filename):
    with open(filename, 'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
    return data

def eval_p(data):
    n_w=0
    n_m=0
    n_n=0
    n_both = 0
    count = 0
    
    for i in range(len(data)):
        count = count+1
        s = data[i][0]
        token = nltk.word_tokenize(s.lower())
        if 'she' in token or 'her' in token or 'woman' in token or 'girl' in token:
            n_w += 1
            if 'he' in token or 'him' in token or 'man' in token or 'boy' in token or 'guy' in token:
                n_m += 1
                n_both += 1
        elif 'he' in token or 'him' in token or 'man' in token or 'boy' in token or 'guy' in token:
            n_m += 1
            if 'she' in token or 'her' in token or 'woman' in token or 'girl' in token:
                n_w += 1
                n_both += 1
        else:
            n_n = n_n+1

    p_w = n_w/count
    p_m = n_m/count
    p_n = n_n/count
    p_both = p_w + p_m + p_n - 1
    print(p_both, n_both/count)
    return np.sqrt(p_w*p_m+p_n), p_m, p_w, p_both, p_n


def write_score(filename):
    trans_en = read_data(filename)
    p, pm, pw, pboth, pn  = eval_p(trans_en)
    return round(p,3), round(pm,3), round(pw,3), round(pboth, 3), round(pn,3)


def main():
    scores = []
    corpus_names = [
        "total_pos.txt",
        "total_neg.txt",
        "total_job.txt",
        "total_informal.txt",
        "total_polite.txt",
        "total_formal.txt"
    ]

    translators = [
        "google", "indictrans2", "gpt35", "gpt4o"
    ]

    for translator in tqdm(translators):
        for corpus in tqdm(corpus_names):
            p, pm, pw, pboth, pn = write_score(f'en_corpus_from_ne/{translator}/{corpus}')
            score = [translator, corpus, p, pm, pw, pboth, pn]
            scores.append(score)


    header = ['Translator', 'Corpus Name', 'P', 'Pm', 'Pw', 'Pboth', 'Pn']
    scores_df = pd.DataFrame(scores, columns=header)
    scores_df.to_csv('TGBI.csv', index=False)
    print("CSV created")

if __name__ == "__main__":
    main()

