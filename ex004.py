n = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(n))
print('Só tem espaço?', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanúmerico?', n.isalnum())
print('Tem maiúsculas?', n.isupper())
print('Tem minúsculas?', n.islower())
print('Tá capitalizada?', n.istitle())
