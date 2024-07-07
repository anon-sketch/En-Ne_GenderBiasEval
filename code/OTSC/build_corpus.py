with open('corpus_occupations.txt', 'r') as occupations_file:
    occupations = occupations_file.readlines()

with open('informal/female_sathi_male.txt', 'w') as male_file, open('informal/female_sathi_female.txt', 'w') as female_file:
    for occ in occupations:
        female_file.write(f"मैले उनलाई लामो समयदेखि चिनेको छु, मेरी साथी {occ.strip()}को रूपमा काम गर्छे।\n")
        male_file.write(f"मैले उनलाई लामो समयदेखि चिनेको छु, मेरा साथी {occ.strip()}को रूपमा काम गर्छ।\n")