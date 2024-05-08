import json

cadastro = [
    {
        "Nome": "Robson",
        "Idade": 40,
        "Profissão": "Programador Python"
    },
    {
        "Nome": "Ana",
        "Idade": 42,
        "Profissão": ["Especialista de Planejamento", "Analista Financeiro"] 
    }
]

print(json.dumps(cadastro,ensure_ascii=False, indent=True))
# ensure_ascii=False - Informa para o código para não tentar codificar os acentos 
