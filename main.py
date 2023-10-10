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
            qt_grupos = int(input("Quantidade de Grupos (Max 10:): "))
            while qt_grupos > 10:
                qt_grupos = int(input("Quantidade de Grupos (Max 10:): "))
            qt_redes_sociais = int(input("Quantidade de Redes Sociais (Max 3): "))
            while qt_redes_sociais > 3:
                qt_redes_sociais = int(input("Quantidade de Redes Sociais (Max 3): "))

            # GERAR DADOS DOS USUÁRIOS
            carregamento("Usuários")
            usuarios = gerar_usuarios(qt_user, qt_grupos)
            exibicao(usuarios, qt_user)

            # GERAR DADOS DOS POSTS
            qt_posts = int(input("Quantidade de posts: "))  # RECEBENDO PARÂMETRO
            carregamento("Posts")
            posts = gerar_post(qt_posts, qt_user, qt_redes_sociais)
            exibicao(posts, qt_posts)

            # GERAR DADOS DOS GRUPOS

            # GERAR REDES SOCIAIS
            carregamento("Redes Sociais")
            redes_sociais = gerar_redes_sociais(qt_redes_sociais)
            exibicao(redes_sociais, qt_redes_sociais)

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
