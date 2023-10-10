from gerar_dados import *

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
            qt_grupos = int(input("Quantidade de Grupos: "))
            qt_redes_sociais = int(input("Quantidade de Redes Sociais (Max 3): "))
            while qt_redes_sociais > 3:
                qt_redes_sociais = int(input("Quantidade de Redes Sociais (Max 3): "))

            # GERAR DADOS DOS USUÁRIOS
            carregamento("Usuários")
            usuarios = gerar_usuarios(qt_user, qt_grupos)
            if usuarios.shape[1] >= 10:
                print("Top 10:\n", usuarios.head(10), "\n")
            else:
                print(f"Top {qt_user}", usuarios.head(qt_user), "\n")

            # GERAR DADOS DOS

        # APAGAR DADOS
        elif escolha == 2:
            pass

        # CONSULTAR DADOS
        elif escolha == 3:
            pass

        # SAIR
        elif escolha == 4:
            exit(0)

    except ValueError:
        print("Valor inválido!")
