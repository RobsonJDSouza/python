from random import choice


class Desenvolvedor:
    def __init__(self, linguagem_programacao=None):
        self.linguagem_programacao = linguagem_programacao
        print(f'Novo desenvolvedor que conhece: \n\t{self.linguagem_programacao}')

    def desenvolvedor_codigo(self):
        print(f'Dev codando em {choice(self.linguagem_programacao)}')

class Gerente:
    def __init__(self, softskills=None):
        self.softskills = softskills
        print(f'Novo gerente com habilidade em: {self.softskills}')
    
    def gerenciar_equipe(self):
        print(f'Gerente está utilizando; {self.softskills}')

class TechLead (Desenvolvedor, Gerente):
    def __init__(self, linguagem_programacao=None, softskills=None):
        Desenvolvedor.__init__(self, linguagem_programacao)
        Gerente.__init__(self, softskills)

tech_lead = TechLead(['C', 'Python'], ['Liderança', 'Comunicação'])
tech_lead.desenvolvedor_codigo()
tech_lead.gerenciar_equipe()