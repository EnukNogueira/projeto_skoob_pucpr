# Skoob CLI - Projeto Somativa PUCPR

Aplicação em Python para gerenciamento de biblioteca pessoal de livros no terminal.

Este projeto foi desenvolvido para a Somativa da PUCPR no curso de Análise e Desenvolvimento de Sistemas, com inspiração no app Skoob.

## Funcionalidades

- Adicionar livros com título e autor.
- Listar todos os livros cadastrados.
- Atualizar dados de um livro (título, autor e status de leitura).
- Remover livros da biblioteca.
- Buscar livros por termo no título.
- Exibir estatísticas da biblioteca (total, lidos e em andamento).
- Persistir os dados em arquivo JSON (`biblioteca.json`).

## Tecnologias

- Python 3
- Bibliotecas padrão: `json`, `os`, `datetime`

## Estrutura do projeto

- `somativa_enuk_skoob.py`: arquivo principal com toda a lógica da aplicação.
- `biblioteca.json`: base de dados local em JSON.
- `README.md`: documentação do projeto.

## Como executar

1. Abra o terminal na pasta do projeto.
2. Execute o comando:

```bash
python somativa_enuk_skoob.py
```

3. Informe seu nome.
4. Use os comandos exibidos no menu.

## Comandos disponíveis

- `ADD`: adiciona um novo livro.
- `LIST`: mostra todos os livros.
- `UPDATE`: altera dados de um livro e registra histórico.
- `DELETE`: remove um livro da lista.
- `SEARCH`: busca por título.
- `STATS`: exibe dados gerais da biblioteca.
- `ABOUT`: mostra uma descrição rápida do projeto.
- `N`: salva os dados e encerra a sessão.

## Formato dos dados (`biblioteca.json`)

Cada livro é salvo com a estrutura abaixo:

```json
{
	"titulo": "Fundacao",
	"autor": "Asimov",
	"lido": false,
	"historico": []
}
```

## Observações

- Na primeira execução, se o arquivo `biblioteca.json` não existir, ele é criado automaticamente ao salvar.
- Se o JSON estiver vazio ou inválido, a aplicação inicia com biblioteca vazia para evitar falhas.

## Autor

- Enuk
