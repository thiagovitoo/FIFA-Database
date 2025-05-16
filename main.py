from src.fifa_database import FIFA_Database
from src.interface import MyApplication

from time import time

import tkinter as tk

# Em caso de atualização de dados, excluir o arquivo data.pkl

# from numba import jit # O @jit compila para código de máquina, aumentando a velocidade de execução.

# Para salvar e carregar dados em arquivos binários, mais eficiente que ler o CSV tudo de novo.
import pickle



def main():
    # Pré-processamento
    start = time()

    fifa_db = FIFA_Database()

    try:
        with open('data/data.pkl', 'rb') as file:
            fifa_db = pickle.load(file)
            # A leitura do arquivo binário foi integrada após a finalização do projeto. Tempo de integração dos 24 milhões de dados anteriores: 54 segundos. Tempo atual após 26 segundos de construção do arquivo binário: 11 segundos.
            print(f'Leitura do arquivo binário: {time() - start:.2f} segundos')

    except FileNotFoundError:
        fifa_db.get_players_info()

        fifa_db.get_tags_info()

        fifa_db.get_rating_info('data/rating.csv')
        leitura_fifa_db = time() - start
        print(f'Leitura do fifa_db: {leitura_fifa_db:.2f} segundos')

        with open('data/data.pkl', 'wb') as file:
            pickle.dump(fifa_db, file)
            print(f'Construção do arquivo binário: {time() - start - leitura_fifa_db:.2f} segundos')

    # Interface gráfica
    root = tk.Tk()
    MyApplication(root, fifa_db)
    root.mainloop()


main()
