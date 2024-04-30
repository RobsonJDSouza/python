'''Um setter (definidor) 
Permite que você configure o valor de um atributo. Por exemplo, se tivermos um atributo "idade" em um objeto chamado "pessoa", um setter poderia ser usado para definir a idade dessa pessoa.

Um getter (obtendor) 
Permite que você obtenha o valor de um atributo. Usando o mesmo exemplo, um getter poderia ser usado para acessar a idade da pessoa.

Eles são úteis porque permitem que você mantenha o controle sobre como os dados são manipulados em sua aplicação, permitindo, por exemplo, validações antes de definir um valor ou calcular um valor dinamicamente antes de retorná-lo. Isso ajuda a manter seu código mais organizado e seguro.'''


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Getter para obter o valor da idade
    def get_idade(self):
        return self.idade

    # Setter para definir o valor da idade
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.idade = nova_idade
        else:
            print("A idade deve ser um número positivo!")

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("João", 30)

# Usando o getter para obter a idade
print("Idade de", pessoa1.nome, ":", pessoa1.get_idade())

# Usando o setter para definir uma nova idade
pessoa1.set_idade(35)

# Usando o getter novamente para verificar a nova idade
print("Nova idade de", pessoa1.nome, ":", pessoa1.get_idade())
