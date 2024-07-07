import ast

with open('nepali_sarkari_jaagirs.txt', 'r') as sarkari_jaagir_file, open('corpus_occupations.txt', 'r') as corpus_occupations:
    sarkari_jaagirs = sarkari_jaagir_file.readlines()
    corpus_occps = corpus_occupations.readlines()

unique_occps = []
for occ in sarkari_jaagirs:
    unique_occ = occ.strip().split("_")[0]
    unique_occps.append(unique_occ)

print(len(unique_occps))
unique_sarkari_jaagirs = list(set(unique_occps))
print(len(unique_sarkari_jaagirs))

total_unique = []
for unique_sarkari_jaagir in unique_sarkari_jaagirs:
    if unique_sarkari_jaagir not in corpus_occps:
        total_unique.append(unique_sarkari_jaagir)

print(len(total_unique))
with open('unique_nepali_occps.txt', 'a') as unique_occps_file:
    for each_occ in total_unique:
        unique_occps_file.write(f"{each_occ}\n")

with open('nepali_sarkari_jaagirs.txt', 'w') as unique_occps_file:
    for each_occ in total_unique:
        unique_occps_file.write(f"{each_occ}\n")
# for occ in new_occps:
#     new_str = occ.split('-')[1].strip()
#     occ_list = ast.literal_eval(new_str)
#     new_occps_list.extend(occ_list)

# print(len(new_occps_list))
# unique_occps_list = list(set(new_occps_list))
# print(len(unique_occps_list))

# with open('unique_nepali_occps.txt', 'a') as op_file:
#     for occ in new_occps_list:
#         op_file.write(f"{occ.strip()}\n")