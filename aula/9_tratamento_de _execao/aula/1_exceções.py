'''
Termo correto para se falar de erro.
Tratar exceção

Obs. Começaremos a analisar o erro de baixo para cima

Documentação Python sobre erros e exceções: 

https://docs.python.org/3/library/exceptions.html
https://docs.python.org/pt-br/3/tutorial/errors.html

ZeroDivisionError: Divisão por zero.
NameError: Nome de variável indefinido.
TypeError: Tipo de dado inválido para uma operação.
ValueError: Valor inválido para uma função ou método.
ImportError: Módulo não encontrado.
IndentationError: Não intendou corretamente o código.


#Exceções de E/S:
IOError: Erro geral de E/S.
OSError: Erro específico do sistema operacional.
FileNotFoundError: Arquivo não encontrado.
PermissionError: Permissão negada.

# Exceções de importação:
ImportError: Módulo não encontrado.
ModuleNotFoundError: Módulo não encontrado (Python 3.6+).

# Exceções de memória:
MemoryError: Memória insuficiente.

# Exceções de tipo:
TypeError: Tipo de dado inválido para uma operação.
ValueError: Valor inválido para uma função ou método.

# Exceções de sintaxe:
SyntaxError: Erro de sintaxe no código.
IndentationError: Erro de indentação.

# Exceções de referência:
NameError: Nome de variável indefinido.
AttributeError: Atributo inexistente.

# Exceções matemáticas:
ZeroDivisionError: Divisão por zero.
OverflowError: Overflow aritmético.
Quando tentamos dividir um número por zero

# Exceções de sistema:
SystemExit: Saída do programa.
KeyboardInterrupt: Interrupção por Ctrl+C.



#### 2. IndexError ou KeyError
Quando tentamos pegar um índice que não existe em uma lista ou uma chave que não existe em um dicionário

#### 3. TypeError ou AttributeError
Quando tentamos atribuir um parâmetro para uma função que não tem parâmetros ou que não possui aquele parâmetro específico ou algum outro erro no parâmetro passado para a função

#### 4. ImportError ou ModuleNotFoundError
Quando tentamos importar um módulo não instalado no nosso computador ou algum objeto/função de um módulo que não existe

#### 5. NameError
Quando tentamos usar uma variável que não existe/não foi iniciada

#### 6. SyntaxError
Quando fizemos algum erro de escrita no código (deixamos de fechar algum parênteses, colchete ou chaves), escrevemos algo que não pode ser escrito ou escrevemos de forma errada

#### 7. IndentationError ou TabError
Quando damos mais ou menos vezes Tab do que deveria em alguma linha de código (mais ou menos indentação)

#### 8. TypeError
Quando tentamos fazer uma operação com um tipo de variável que não pode ser feito nela, ex: tentamos pegar o índice de um item de uma variável que é inteiro (ao invés de uma lista). Como números inteiros não são listas, teremos um typeerror 
#### 9. UnicodeError

Quando o programa não conseguiu usar o método de encoding correto. Normalmente isso sinaliza a existência de algum caractere especial como ~, ç, etc. que está atrapalhando o código.

#### 10. ValueError
Quando passamos um valor que não pode ser passado para uma função ou método.

'''