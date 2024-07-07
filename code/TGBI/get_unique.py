import os

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def process_files(english_folder, nepali_folder):
    nepali_files = os.listdir(nepali_folder)
    english_files = os.listdir(english_folder)
    print(nepali_files)

    for nepali_file in nepali_files:
        # if nepali_file in english_files:
            nepali_path = os.path.join(nepali_folder, nepali_file)
            # english_path = os.path.join(english_folder, nepali_file)

            print(nepali_path)
            nepali_lines = read_file(nepali_path)
            # english_lines = read_file(english_path)
            print(nepali_lines.index)

            unique_nepali_lines = list(set(nepali_lines))  # Get unique lines in Nepali file
            unique_nepali_lines.sort(key=nepali_lines.index)  # Maintain original order

            with open(nepali_path, 'w') as testfile:
                for sentence in unique_nepali_lines:
                    testfile.write(f"{sentence.strip()}\n")

            # # Find corresponding English lines
            # unique_english_lines = []
            # for line in unique_nepali_lines:
            #     index = nepali_lines.index(line)
            #     unique_english_lines.append(english_lines[index])

            # # Write unique lines back to the English file
            # write_file(english_path, unique_english_lines)
            print(f'Processed file: {nepali_file}')

english_folder = 'en_corpus_from_ne/test'
nepali_folder = 'ne_corpus/test'

process_files(english_folder, nepali_folder)
