from math import radians, sin, cos, tan
num = (float(input('Digite um ângulo: ')))
sin = sin(radians(num))
cos = cos(radians(num))
tan = tan(radians(num))
print('O ângulo {} possui o SENO de: {:.2f}'.format(num,sin))
print('O ângulo {} possui o COSSENO de: {:.2f}'.format(num,cos))
print('O ângulo {} possui o TANGENTE de: {:.2f}'.format(num,tan))