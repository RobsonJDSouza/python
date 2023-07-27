#modulo são bibliotecas  - 
#existe duas maneiras de importar
#import robson
#from robson import olho

#Modulo
'''
import math - importa toda biblioteca
from math import sqrt - importa apenas a necessidade
from math import ctrl + espaço mostra todas a biblioteca
https://docs.python.org/3.10/library/numeric.html

'''
#Exemplo
import math 
x = 25
raiz = int(math.sqrt(x))
print(raiz)

import math as m # alias
y = 25
raiz = int(m.sqrt(x))
print(raiz)

from math import sqrt, ceil # Podemos colocar quantos objetos necessário
z = 25
raiz = int(sqrt(x))
print(raiz)


from math import sqrt as s #alias
r = 25
raiz = int(s(x))
print(raiz)

print()
