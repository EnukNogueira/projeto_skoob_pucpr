from datetime import datetime
from typing import List, Optional, Dict, Any
import json
import os

"""Projeto de Somativa 2 da PUCPR, foi utilizado a base da somativa 1, formativa 4,5,6 e cursos da ALURA para criar esse código. 
Antes ele criava um projeto porem como eu gosto batante de ler resolvi mudar para livros. 
Inspiração para o projeto: App skoob."""


class Book:
    """Representa um livro na biblioteca."""
    
    def __init__(self, title: str, author: str = "") -> None:
        """Inicializa um novo livro."""
        self.title: str = title
        self.author: str = author
        self.is_read: bool = False
        self.history: List[tuple] = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Converte o livro para dicionário."""
        return {
            'titulo': self.title,
            'autor': self.author,
            'lido': self.is_read,
            'historico': self.history
        }
    
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Book':
        """Cria um livro a partir de um dicionário."""
        book = Book(data.get('titulo', ''), data.get('autor', ''))
        book.is_read = data.get('lido', False)
        book.history = data.get('historico', [])
        return book


def convert_to_bool(value: str) -> bool:
 
    return value.strip().lower() in ("s", "sim", "true", "1", "t", "y", "yes")


def load_library(filename: str = "biblioteca.json") -> List[Book]:
    """Carrega a lista de livros de um arquivo do JSON."""
    try:
        if not os.path.exists(filename):
            print("Primeira vez aqui! Criando sua biblioteca...")
            return []
        
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not isinstance(data, list):
                print("AVISO: formato do JSON inválido. Iniciando com a biblioteca vazia.")
                return []
            return [Book.from_dict(item) for item in data]
    
    except json.JSONDecodeError:
        print("ERRO: arquivo JSON está com problemas ou vazio. Iniciando com a biblioteca vazia.")
        return []
    except Exception as e:
        print(f"Erro ao carregar arquivo: {e}. Iniciando com a biblioteca vazia.")
        return []


def save_library(book_list: List[Book], filename: str = "biblioteca.json") -> None:
    """Salva a lista de livros em um arquivo em formato JSON."""
    try:
        data = [book.to_dict() for book in book_list]
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Biblioteca salva com sucesso em '{filename}'!")
    except Exception as e:
        print(f"Erro ao salvar biblioteca: {e}")


def find_book(book_list: List[Book], title: str) -> Optional[Book]:
 
    for book in book_list:
        if book.title.lower() == title.lower():
            return book
    return None



def add_book(book_list: List[Book]) -> None:
    """Adiciona um livro novo à biblioteca."""
    try:
        title = input('Título do livro: ').strip()
        if not title:
            print("Erro: Digite o título do livro.")
            return
        
        if find_book(book_list, title) is not None:
            print(f"Erro: livro '{title}' já existe no banco de dados do projeto.")
            return
        
        author = input('Autor (opcional): ').strip()
        
        book = Book(title, author)
        book_list.append(book)
        print('Livro adicionado com sucesso!')
    
    except Exception as e:
        print(f"Erro ao adicionar livro: {e}")


def list_books(book_list: List[Book], user_name: str) -> None:
    """Lista todos os livros da biblioteca."""
    if len(book_list) == 0:
        print('Não tem livros na lista')
    else:
        print(f"\nHistórico de livros de {user_name}:")
        for counter, book in enumerate(book_list, start=1):
            status = 'Lido' if book.is_read else 'Não lido'
            print(f"{counter}. Título: {book.title}")
            if book.author:
                print(f"   Autor: {book.author}")
            print(f"   Lido: {status}")
            if book.history:
                print(f"Histórico: {book.history}")
            else:
                print(f"Histórico: sem os dados")


def about() -> None:
    """Exibe informações sobre o código."""
    print('\nSobre o Código:')
    print('Este código cadastra, lista, atualiza e remove livros.') #Inspirado no app Skoob ao qual uso para anotar os livros que estou lendo ou que pretender ler no futuro.
    print('Os dados são persistidos em um arquivo JSON chamado "biblioteca.json".')



def update_book(book_list: List[Book]) -> None:
    """Atualiza as informações de um livro."""
    try:
        title_update = input('Qual livro você deseja alterar? ').strip()
        if not title_update:
            print("Erro: título inválido.")
            return
        
        book = find_book(book_list, title_update)
        if book is None:
            print('Livro não encontrado.')
            return

        new_title = input(f'Novo título (Enter para alterar "{book.title}"): ').strip()
        if not new_title:
            new_title = book.title

        new_author = input(f'Novo autor (Enter para alterar "{book.author}"): ').strip()
        if not new_author:
            new_author = book.author

        new_status_text = input('Você já leu esse livro? (s/n): ').strip()
        new_status = convert_to_bool(new_status_text)
        change_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S') #Foi utilizado IA para aprender como usar essa biblioteca, pois não sabia como puxar a data e hora do computador do usuario, logo pedi uma explicacao de como fazer isso e descobri que era assim como podem ver no código.

        book.title = new_title
        book.author = new_author
        book.is_read = new_status
        book.history.append((change_date, new_status, new_title))
        print('Livro atualizado com sucesso!')
    
    except Exception as e:
        print(f"Erro ao atualizar livro: {e}")


def delete_book(book_list: List[Book]) -> None:
    """Deleta um livro da biblioteca."""
    try:
        title_remove = input('Qual livro deseja deletar? ').strip()
        if not title_remove:
            print("Erro: título inválido.")
            return
        
        book = find_book(book_list, title_remove)
        if book is None:
            print('Livro não foi encontrado.')
            return

        book_list.remove(book)
        print(f'Livro "{book.title}" deletado com sucesso!')
    
    except Exception as e:
        print(f"Erro ao deletar livro: {e}")


def display_stats(book_list: List[Book]) -> None:
    """Exibe os dados da biblioteca de livros."""
    if len(book_list) == 0:
        print("Nenhum livro para exibir os dados.")
        return
    
    completed = sum(1 for book in book_list if book.is_read)
    in_progress = len(book_list) - completed
    
    print("\n=== DADOS DA BIBLIOTECA ===")
    print(f"Total de livros: {len(book_list)}")
    print(f"Livros lidos: {completed}")
    print(f"Livros em andamento: {in_progress}")
    
    if completed > 0:
        last_completion = None
        for book in book_list:
            if book.is_read and book.history:
                if last_completion is None or book.history[-1][0] > last_completion:
                    last_completion = book.history[-1][0]
        if last_completion:
            print(f"Última leitura concluída em: {last_completion}")


def search_books(book_list: List[Book]) -> None:
    """Busca livros pelo título."""
    try:
        term = input('Digite o termo de busca (título): ').strip().lower()
        if not term:
            print("Erro: termo de busca não pode estar vazio.")
            return
        
        results = [book for book in book_list if term in book.title.lower()]
        
        if not results:
            print(f"Nenhum livro encontrado com o termo '{term}'.")
        else:
            print(f"\n=== RESULTADOS DA BUSCA ({len(results)} encontrado(s)) ===")
            for counter, book in enumerate(results, start=1):
                status = 'Lido' if book.is_read else 'Em andamento'
                line = f"{counter}. {book.title} - {status}"
                if book.author:
                    line += f" (Autor: {book.author})"
                print(line)
    
    except Exception as e:
        print(f"Erro ao buscar: {e}")



def main() -> None:
    """Função principal do aplicativo."""
    user_name = str(input('Escreva seu nome: ')).strip()
    book_list = load_library()

    while True:
        print("REGRAS")
        print("ADD(Adicionar), LIST(Listar), UPDATE(Atualizar), DELETE(Apagar), STATS(Status), SEARCH(Pesquisar), ABOUT(Sobre) ou N(sair)")

        command = input('O que deseja fazer agora? ').upper()

        if command == 'N':
            print(f'Finalizando sessão, {user_name}...')
            save_library(book_list)
            break

        elif command == 'ADD':
            add_book(book_list)

        elif command == 'LIST':
            list_books(book_list, user_name)

        elif command == 'UPDATE':
            update_book(book_list)

        elif command == 'DELETE':
            delete_book(book_list)

        elif command == 'ABOUT':
            about()
        
        elif command == 'STATS':
            display_stats(book_list)
        
        elif command == 'SEARCH':
            search_books(book_list)

        else:
            print('Opção invalida por favor tente novamente.')


if __name__ == '__main__':
    main()

