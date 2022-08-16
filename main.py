import os

diretorio_downloads = "C:/Users/dacma/Downloads"
arquivos = os.listdir(diretorio_downloads)

for arquivo in arquivos:
    nome = f'{diretorio_downloads}/{arquivo}'
    tamanho = os.path.getsize(nome) / 1000000 #tamanho em megabytes
    if tamanho > : #tem que colocar o tamanho que eu quero que delete aqui
        os.remove(nome)