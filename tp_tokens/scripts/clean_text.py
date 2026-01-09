import re
import os

# Liste des regexps à nettoyer dans les textes

def clean_text(text:str):
    
    header_re = re.compile(r'---.*?---', re.DOTALL)
    title_re = re.compile(r'[#|\*].*?\n')
    html_re = re.compile(r'<.*?>\n')
    article_re = re.compile(r'\s[LDR]\.\s[0-9\-]+')
    numerotation1_re = re.compile(r'\n\d+°\s')
    numerotation2_re = re.compile(r'\n[a-zA-Z]+\)\s')
    numerotation3_re = re.compile(r'\n[IVXLCDM]+\.\s[—|-|–]\s')
    newline_re = re.compile(r'(?<=\n)\n+')

    text = header_re.sub('', text)  
    text = title_re.sub('', text)
    text = html_re.sub('', text)
    text = article_re.sub(' ', text)
    text = numerotation1_re.sub('', text)
    text = numerotation2_re.sub('', text)
    text = numerotation3_re.sub('', text) 
    text = newline_re.sub('', text)

    return text


if __name__ == "__main__":
    codes_list = os.listdir('codes/')
    os.makedirs('clean_codes/', exist_ok=True)
    print(f'Cleaning {len(codes_list)} files...')
    for code in codes_list:
        with open(f'codes/{code}', 'r', encoding='utf-8') as f:
            text = f.read()
        cleaned_text = clean_text(text)
        with open(f'clean_codes/{code[:-3]}.txt', 'w', encoding='utf-8') as f:
            f.write(cleaned_text)
