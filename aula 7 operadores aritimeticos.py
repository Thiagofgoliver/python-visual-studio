#operadores aritimeticos

# +  adição 
# - subtração
# * multiplicação 
# / divisão 
# ** potencia ao quadrado 
# // divisão inteira
# % resto da divisão 
# oque é divisão inteira e resto da divisão ? operando  pode ser variavel e pode ser numero
#funciona como se fosse operador binarios  um operador que precisa de 2 operando 
# exemplo :

#5+2
#7
#5-2 
#3
#5//2
#2
#5%2
#1


#ordem de precedencia
#1 ()
#2 **
#3 * / // %
#4 +-

# operador com str
#/n  para quebrar  linha
# end = '' para nao quebrar linha 

n1 =int (input('um valor:'))
n2 = int (input('outro valor:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2 

print ('a soma {} , \n o produto é {} ea divisao é {:.3f}'.format (s, m , d ), end = '>>>>>')
print('divisao inteira é {}e potencia {}'.format(di,e))
