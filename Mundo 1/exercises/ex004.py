texto = input("DIGITE ALGO: ")
print('--Tipo primitivo: ', type(texto))
print('--São só espaços? ', texto.isspace())
print('--São só números? ', texto.isnumeric())
print('--São só letras? ', texto.isalpha())
print('--Possui somente letras ou números? ', texto.isalnum())
print('--Somente a primeira letra é maiúscula? ', texto.istitle())
print('--Todos caracteres são maiúsculos? ', texto.isupper())
print('--Todos caracteres são minúsculos? ', texto.islower())