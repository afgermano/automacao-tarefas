# 📝 Sistema de automação de tarefas.

Projeto criado para automatizar o cadastro de produtos, utilizando Python e as bibliotecas PyAutoGui e Pandas.

## Estrutura do Projeto

```
.
├── main.py        # Script principal que executa a automação de cadastro
├── position.py    # Script auxiliar para descobrir coordenadas do mouse
├── produtos.csv   # Base de dados com os produtos a serem cadastrados
└── README.md      # Documentação do projeto
```

## Como Funciona

1. O script abre o navegador Chrome.
2. Acessa a página de login do sistema.
3. Preenche e-mail e senha automaticamente.
4. Lê o arquivo `produtos.csv`.
5. Para cada linha da tabela:
   - Preenche os campos do formulário
   - Envia o cadastro
   - Volta para o topo da página
6. Repete o processo até cadastrar todos os produtos.

## Créditos

Esse projeto foi desenvolvido durante um evento feito pelo canal "Hashtag Programação".

O objetivo do projeto foi praticar conceitos de automação com PyAutoGUI e manipulação de dados com Pandas, automatizando o cadastro de produtos em um sistema web.

Algumas adaptações e melhorias foram feitas posteriormente para organização do código e estrutura do projeto.
