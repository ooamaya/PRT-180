from collections import defaultdict

result = defaultdict(dict)
current_key = None

with open('Input.txt',mode='r',encoding='utf-8') as input:
    data=input.read()
#Convertir el archivo txt en un diccionario con los mismos niveles
for line in data.splitlines():
    if not line: continue 
    if line[0]!='•':
        current_key = line.replace(':','')
        continue
    line=line.replace('• ','').replace('•','').strip()
    array = line.split(": ")
    result[current_key][array[0]]=array[1]
#Creacion de un nuevo diccionario con las nuevas agrupaciones.    
dict_1 = {}
for key in result:
    key1 = result[key]['Fabricante']
    key2 = result[key]['Categoría']
    key3 = result[key]['Género']
    if key1 not in dict_1:
        dict_1[key1]={}    
    if key2 not in dict_1[key1]:
        dict_1[key1][key2]={}
    if key3 not in dict_1[key1][key2]:
        dict_1[key1][key2][key3]=[]
    dict_1[key1][key2][key3].append(key)  
print(dict_1)
