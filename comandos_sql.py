from main import *


################################
#             CRUD             #
################################

cursor = con.cursor()


def select(campos, tabela, where=None):
    """
    :param campos: Campos que queremos consultar
    :param tabela: Tabelas que queremos consultar
    :param where: Condição
    :return: Retorno da Query do BD
    """
    query = f"SELECT {campos} FROM {tabela}"
    if where:
        query = f"{query} WHERE {where}"
    cursor.execute(query)
    return cursor.fetchall()


def consulta(tabela):
    """
    :param tabela:{
    1: Usuários
    2: Posts
    3: Grupos
    4: Redes Sociais
    }
    :return:
    """
    try:
        while True:
            if tabela == 1:  # USUÁRIOS
                campos_dict = {
                    "0": "id",
                    "1": "nome",
                    "2": "email",
                    "3": "telefone",
                    "4": "id_grupo"
                }
                campos = str(input("Selecione os campos:"
                                   "0 - id"
                                   "1 - nome"
                                   "2 - email"
                                   "3 - telefone"
                                   "4 - id_grupo"
                                   "Exemplo: > 1, 2, 3 (separados por vírgula)"
                                   "> "))

                select(campos="", tabela="usuarios")
    except ValueError:
        print("Valor inválido")
