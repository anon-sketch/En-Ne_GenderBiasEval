with open("../ne_corpus/total_formal.txt", 'r') as occ_file:
    sentences = occ_file.readlines()

with open('corpus_occupations.txt', 'w') as outfile:
    for sentence in sentences[:998]:
        occupations = (sentence.strip()).split(" ")
        if occupations[-1] == "हुनुहुन्छ":
            outfile.write(f"{' '.join(occupations[1:-1])}\n")
