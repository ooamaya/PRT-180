import re
from collections import OrderedDict,Counter

with open('text_in.txt') as input:
    contents=input.read()
words = []
with open('text_in.txt') as input:
    words = [re.sub("\n","", _) for _ in input.readlines()]
no_words_input=words[0]
No_lines = len (open('text_in.txt').readlines()) -1
if no_words_input.isdigit()==False:
    print('La primera linea del archivo debe ser un entero, con el numero de palabras del archivo')
elif int(no_words_input)!=No_lines:
    print(f'El numero de palabras ({No_lines}) es distinto al valor puesto en la primera linea del archivo ({no_words_input})')
else:
    words.pop(0)
    words_unique=OrderedDict.fromkeys(words).keys()
    count_unique_words = len(words_unique)
    linea_dos=''
    word_counts = Counter(words)
    for word, count in word_counts.items():
        if len(linea_dos)==0:
            linea_dos = linea_dos + str(count)
        else:
            linea_dos = linea_dos + ' ' + str(count)
    output= open("text_out.txt","w+")
    output.write(str(count_unique_words)+"\n")
    output.write(linea_dos)