translators = ['gpt4o', 'google','indictrans2']

index = 1292
for translator in translators:
    with open(f'{translator}/formal/female_sathi_female.txt', 'r') as inputfile:
        sentences = inputfile.readlines()
        print(sentences[index])