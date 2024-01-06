# Gerenciador de acervo de filmes

Este projeto consiste em um programa que permite armazenar, consultar, deletar e alterar filmes de uma base de dados.

### Requisitos obrigatórios
- [x] O sistema precisa incluir informações de título, gênero, ano e avaliação dos filmes.
- [x] CRUD: O sistema precisa incluir funções de criar, atualizar, listar, deletar e pesquisar filmes.

### Adicionais
- [x] Serialização dos dados em json ou formato desejado
- [x] Listagem paginada
- [x] Listagem com agrupamento por gênero, ano ou avaliação
- [ ] Teste unitário

### Como configurar o ambiente
1. Ter o Python instalado no seu computador (para o desenvolvimento dessa aplicação foi usada a versão 3.11.2).

2. Clonar o repositório:
```bash
git clone https://github.com/viquiiz/python-gestao-filmes.git
``` 

3. Abrir a pasta na IDE de sua escolha e instalar as bibliotecas contidas no arquivo requirements.txt via terminal:
```bash
pip install -r requirements.txt
```

### Como rodar

1. Na pasta raiz do projeto, rodar o arquivo main.py:
```bash
python main.py
```