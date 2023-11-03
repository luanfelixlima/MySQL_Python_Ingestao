from gerar_dados import *
from visuais import *
from comandos_sql import *
import mysql.connector

# PARÂMETROS DA CONEXÃO
while True:
    print(f"{'=' * 40} Alimentando Banco de dados v1.0 {'=' * 40}")
    print("-> Dados do Banco MySQL <-")
    host = str(input("[Host] > "))
    database = str(input("[Database] > "))
    user = str(input("[User] > "))
    password = str(input("[Pass] > "))
    print("")
    break

# CONEXÃO
con = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

# PROGRAMA
while True:
    try:
        escolha = int(input("======================\n"
                            "[1] - Gerar dados    |\n"
                            "[2] - Apagar dados   |\n"
                            "[3] - Consultar dados|\n"
                            "[4] - Sair           |\n"
                            "======================\n"
                            ">>> "))
        # GERAR DADOS
        if escolha == 1:

            # RECEBENDO PARAMÊTROS
            qt_user = int(input("Quantidade de usuários: "))
            qt_grupos = int(input("Quantidade de Grupos (Max 10:): "))
            while qt_grupos > 10:
                qt_grupos = int(input("Quantidade de Grupos (Max 10:): "))
            qt_redes_sociais = int(input("Quantidade de Redes Sociais (Max 3): "))
            while qt_redes_sociais > 3:
                qt_redes_sociais = int(input("Quantidade de Redes Sociais (Max 3): "))
            qt_posts = int(input("Quantidade de posts: "))

            # GERAR DADOS DOS USUÁRIOS
            carregamento("Usuários")
            usuarios = gerar_usuarios(qt_user, qt_grupos)
            exibicao(usuarios, qt_user)

            # GERAR DADOS DOS POSTS
            carregamento("Posts")
            posts = gerar_post(qt_posts, qt_user, qt_redes_sociais)
            exibicao(posts, qt_posts)

            # GERAR DADOS DOS GRUPOS
            carregamento("Grupos")
            grupos = gerar_grupos(qt_grupos)
            exibicao(grupos, qt_grupos)

            # GERAR REDES SOCIAIS
            carregamento("Redes Sociais")
            redes_sociais = gerar_redes_sociais(qt_redes_sociais)
            exibicao(redes_sociais, qt_redes_sociais)

        # APAGAR DADOS
        elif escolha == 2:
            apagar = int(input("\n=== Escolher Tabela ===\n"
                               "[1] - TABLE Usuarios  |\n"
                               "[2] - TABLE Posts     |\n"
                               "[3] - TABLE Grupos    |\n"
                               "[4] - TABLE Sociais   |\n"
                               "=======================\n"
                               ">>> "))

        # CONSULTAR DADOS
        elif escolha == 3:
            query_tabela = int(input(f"===== Consulta do BD: {database} =====\n"
                                     "[1] - TABLE Usuarios         \n"
                                     "[2] - TABLE Posts            \n"
                                     "[3] - TABLE Grupos           \n"
                                     "[4] - TABLE Sociais          \n"
                                     "===================================\n"
                                     ">>> "))
            consulta(query_tabela)

        # SAIR
        elif escolha == 4:
            exit(0)

    except ValueError:
        print("Valor inválido!")
