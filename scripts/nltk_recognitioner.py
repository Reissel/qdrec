import pandas as pd
import nltk

"""

    Run this block on first execution to make
    nltk downloader install its dependencies

    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')

"""

df = pd.read_csv('../dataset-ambiental.csv')

i = 0

for excerpt in df.excerpt:
    if i == 1:
        break
    print( 'Trecho: ' + excerpt )
    tokens = nltk.word_tokenize( excerpt, language='portuguese' )
    tagged = nltk.pos_tag( tokens )
    entities = nltk.chunk.ne_chunk( tagged )
    print( entities )
    i += 1