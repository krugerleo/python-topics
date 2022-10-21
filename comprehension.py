obj = {
    'key':'value',
    'key':'Doublevalue',
    'chave':'valor',
    'kage': 'sei la',
    'val1': 1,
    'val2': 2
}

##Comprehension with If-clause:
integers = [ obj[item] for item in obj if type(obj[item]) == int ]
print(integers)

##Dictionary Comprehension:
chaves = {key for key in obj}
print(chaves)
teste = { key:obj[key] for key in obj }
teste2 = { obj[key] for key in obj }
print(teste)
print(teste2)

## Generator Comprehension:
teste = ((key) for key in obj)    
for i in teste:
    print(i)

## Multiple Comprehension:    
values = [(x,y) for x in range(5) for y in range(3)]
values = []
for x in range(5):
    for y in range(3):
        values.append((x,y))