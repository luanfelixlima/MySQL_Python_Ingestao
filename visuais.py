from time import sleep


def aviso(tabela):
    print(f"\nTodos os dados da tabela \"{tabela}\" serão apagados!\n"
          "Deseja continuar? (n/s)")
    sair = str(input("> ")).lower()
    while sair != "s" and sair != "n":
        sair = str(input("> ")).lower()
    if sair == "s":
        print("Dados apagados! Alteração realizada! Voltando para o menu...\n")
    elif sair == "n":
        print("Nenhuma alteração realizada! Voltando para o menu...\n")


def carregamento(dado):
    print(f"{'-'* 60}")
    print(f"\nGerando {dado}.")
    sleep(0.5)
    print(f"Gerando {dado}..")
    sleep(0.5)
    print(f"Gerando {dado}...\n")


def exibicao(dados, qt):
    if dados.shape[0] >= 10:
        print(f"{dados.shape[0]} Linhas e {dados.shape[1]} Colunas geradas!\n"
              f"Top 10:\n", dados.head(10), "\n")
    else:
        print(f"{dados.shape[0]} Linhas e {dados.shape[1]} Colunas geradas!\n"
              f"Top {qt}\n", dados.head(qt), "\n")
