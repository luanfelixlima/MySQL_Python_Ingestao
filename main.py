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
            pass

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
