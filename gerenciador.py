import os

def listar_documentos(pasta):
    for raiz, dirs, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            tipo = os.path.splitext(arquivo)[1]
            print(f"{arquivo} | Tipo: {tipo}")

def adicionar_documento(origem, destino):
    os.rename(origem, destino)

def renomear_documento(antigo, novo):
    os.rename(antigo, novo)

def remover_documento(caminho):
    os.remove(caminho)

if __name__ == "__main__":
    print("Sistema de Biblioteca Digital")
    print("1 - Listar\n2 - Adicionar\n3 - Renomear\n4 - Remover")
    op = input("Escolha uma opção: ")
    
    if op == "1":
        pasta = input("Digite o caminho da pasta: ")
        listar_documentos(pasta)
    elif op == "2":
        origem = input("Caminho do arquivo: ")
        destino = input("Novo nome/caminho: ")
        adicionar_documento(origem, destino)
    elif op == "3":
        antigo = input("Arquivo atual: ")
        novo = input("Novo nome: ")
        renomear_documento(antigo, novo)
    elif op == "4":
        caminho = input("Arquivo a remover: ")
        remover_documento(caminho)
    else:
        print("Opção inválida.")
