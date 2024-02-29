# LANÇAR EXCEÇÕES


#Nome,idade,email
cadastro_csv = [
    'Robson,40,robson@hotmail.com',
    'Ana,42,ana@gmail.com', 
    'Sofia,8s,ana@gmail.com' #Usuário faltou acrescentar o email / Usuário colocou uma string no inteiro
]

def processando_dados(cadastros):
    for cadastro in cadastros:
        dados = cadastro.split(',')

        if len(dados) != 3:
            raise IndexError("Fomato incorreto dos dados")
        
        nome = dados[0]
        
        try:
            idade = int(dados[1])
        except ValueError:
            raise ValueError ('Erro no formato do dado')

        
        email = dados[2]
        print(f'{nome} tem {idade} anos e possui o {email}')

try:
    processando_dados(cadastro_csv)

except IndexError as excecao:
   print(f'Vai arrumar o código!! Esse é o erro {excecao}')