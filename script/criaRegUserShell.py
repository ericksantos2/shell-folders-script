from fn import (criaLista, criaArquivo)
from file import File
from criaRegShellFolders import shellFoldersApp


file = File('User Shell Folders.reg')


def app(pathInicial):
    path = pathInicial
    if path[len(path) - 1] != '\\':
        path += '\\'
    lista = criaLista(path)
    criaArquivo(lista, file)
    msg = input('Você deseja que também seja criado um arquivo para Shell Folders?\n(essa opção não é recomendada para quem tem mais de um usuário no computador)\n(S/n) ').lower()
    if msg == 's':
        shellFoldersApp(path)
