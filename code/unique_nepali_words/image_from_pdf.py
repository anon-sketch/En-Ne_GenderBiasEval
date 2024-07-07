from pdf2image import convert_from_path
import pytesseract
from tqdm import tqdm

# 1. Getting pdf
filePath = 'ne-en-bias-eval/sarkari_jobs/नेपाल_शिक्षा_सेवा_गठन_समूह_तथा_श्रेणी_विभाजन_र_नियुक्ति_नियमहरू.pdf'
doc = convert_from_path(filePath)

# 2. Convert PDF to images
pages = convert_from_path(filePath)
print("Converted pdf to images")

print("\n Converting image to csv")
for i, page in enumerate(tqdm(pages[8:14])):
    # 4. Extract text from image
    extracted_string = pytesseract.image_to_string(page, lang='nep')
    with open('output_text.txt', 'a') as out_file:
        out_file.write(extracted_string)