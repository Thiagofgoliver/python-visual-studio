#faça um programa que escreva um programa na tela e fale o tipo primitivo 


a = input ('digite algo :  ')
print ('tipo primitivo desse valor é ',type(a))

print ('so tem espaços?' , a.isspace())

print ('é um numero ' , a.isnumeric())

print ('é alfabetico ?' , a.isalpha())

print ('é alfanumerico ?' , a.isalnum())


print ('está em maiusculo ?' , a.isupper())


print ('está em minusculo ?' , a.islower())

#capitalizada quando está em maiuscula e minuscula

print ('está capitalizada ?' , a.istitle())
