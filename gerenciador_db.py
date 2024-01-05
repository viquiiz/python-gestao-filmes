import json

#função para abrir o arquivo json
def abrir_db():
    with open('db.json', 'r') as f:
        return json.load(f)

#função para atualizar o arquivo json
def atualizar_db(filme):
    with open('db.json', 'w') as f:
        return json.dump(filme, f)
    
def print_padrao(filme):
    print(f"""
Id: {filme['id']} 
Nome: {filme['nome']}
Gênero: {filme['genero']}
Ano: {filme['ano']}
Nota: {filme['nota']}
""")