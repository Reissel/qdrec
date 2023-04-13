import pandas as pd
import nltk
import unidecode as ud

def contains_word(s, w):
    return f' {w} ' in f' {s} '

def foundInNames(namesList, searchedElement, i):
    normalized = ud.unidecode(searchedElement)
    for line in namesList:
        if contains_word(normalized.lower(),line.lower()):
            print('Found with ' + line + ' in name: ' + searchedElement + ' in excerpt number: ' + str(i))
            return searchedElement
    return ''

i = 0

with open('../LEX_NOMES_BR_ORDERED.txt') as file:
    lines = [line.rstrip() for line in file]


df = pd.read_csv('../dataset-ambiental.csv')

for excerpt in df.excerpt:
    if i == 100:
        break
    string = str(excerpt).replace('- ', '')
    palavras = nltk.word_tokenize(string, language='portuguese')
    
    palavras_etiquetadas = nltk.pos_tag(palavras)
    found_names = []
    for palavra_etiquetada in palavras_etiquetadas:
        if palavra_etiquetada[1] == 'NNP' or palavra_etiquetada[0].isupper():
            returned_name = foundInNames(lines, palavra_etiquetada[0], i)
            if returned_name != '' and returned_name not in found_names:
                found_names.append(returned_name)
            #print(palavra_etiquetada)

    if len(found_names) != 0:
        names = ''
        for name in found_names:
            names += name + ' '
        with open('excerpts.txt', 'a+', encoding='utf-8') as f:
            f.write(names + '\n')
    
    i += 1
