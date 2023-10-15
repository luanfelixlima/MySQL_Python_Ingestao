from random import choice as cc
from random import randint
from datetime import date
import pandas as pd

global chave

# modelo de alimentação:
"""
#### usuarios ####
id = null (auto_increment)
nome = nome + sobrenome
email = nome + email
telefone = random
id _grupo = random
"""
"""
#### posts ####
id = null (auto increment)
id_user = random -> quantidade de user
conteudo = conteudos
data_post = random datetime
"""
"""
#### grupos ####
id = null (auto_increment)
id_user = random -> quantidade de user
nome = random nomes de grupos
desc = random temas de trends
"""

# usuarios
emails = [
    "@gmail.com", "@outlook.com", "@amazon.com", "@yahoo.com.br"
]
nomes = [
    "Sofia", "João", "Ana", "Pedro", "Maria", "Lucas", "Beatriz", "Guilherme",
    "Laura", "Matheus", "Isabella", "Leonardo", "Gabriela", "Enzo", "Valentina",
    "Carlos", "Clara", "Miguel", "Eloá", "Rafael", "Manuela", "Daniel", "Júlia",
    "Bruno", "Helena", "Gustavo", "Mariana", "Felipe", "Larissa", "André", "Luiza",
    "Thiago", "Yasmin", "Alexandre", "Camila"
]
sobrenomes = [
    "Silva", "Santos", "Oliveira", "Pereira", "Ferreira", "Rodrigues", "Almeida",
    "Souza", "Costa", "Carvalho", "Gomes", "Martins", "Araújo", "Lima", "Rocha",
    "Mendes", "Barbosa", "Dias", "Nunes", "Cavalcanti", "Monteiro", "Freitas",
    "Ribeiro", "Pinto", "Cardoso", "Cruz", "Moura", "Castro", "Gonçalves", "Ramos",
    "Lopes", "Correia", "Teixeira", "Machado", "Vieira", "Fernandes", "Azevedo"
]


class Usuarios:
    def __init__(self, quantidade_grupos):
        """
        :param quantidade_grupos: quantidade de grupos que terá no BD
        """
        primeiro_nome = cc(nomes)  # nome aleatório
        sobrenome = cc(sobrenomes)  # sobrenome aleatório
        self.nome = primeiro_nome + " " + sobrenome  # Nome Completo
        self.email = primeiro_nome.lower() + sobrenome.lower() + cc(emails)  # nome + sobrenome + email aleatório
        self.telefone = str(randint(90000, 99999)) + "-" + str(randint(1000, 9999))  # Número de Telefone aleatório
        self.id_grupo = randint(1, quantidade_grupos)  # Id de grupo aleatório baseado na quantidade de grupo


# Posts
conteudo = [
    "Estou radiante!",
    "Que alegria!",
    "Estou nas nuvens!",
    "Isso é incrível!",
    "Estou sorrindo de orelha a orelha!",
    "Felicidade pura!",
    "Estou tão feliz que não consigo conter!",
    "É um sonho realizado!",
    "Estou pulando de alegria!",
    "Isso fez o meu dia!",
    "Estou de coração partido.",
    "Que tristeza profunda.",
    "Sinto como se o mundo estivesse desabando.",
    "Estou me sentindo melancólico.",
    "Às vezes, a vida é tão cruel.",
    "Estou me sentindo vazio por dentro.",
    "Essa notícia me deixou arrasado.",
    "É difícil segurar as lágrimas.",
    "Estou em um momento difícil.",
    "Às vezes, a tristeza é inevitável.",
    "Estou furioso!",
    "Que raiva!",
    "Estou prestes a explodir!",
    "Não posso acreditar no que aconteceu!",
    "Estou com ódio dessa situação.",
    "Essa injustiça me deixa louco.",
    "Estou fervendo de raiva por dentro.",
    "Preciso me acalmar antes de fazer algo impulsivo.",
    "Não posso suportar isso mais!",
    "Estou com uma raiva que não passa.",
    "Uau, que surpresa!",
    "Não estava esperando por isso!",
    "Estou boquiaberto!",
    "Inacreditável!",
    "Que choque!",
    "Estou sem palavras!",
    "Isso é realmente surpreendente!",
    "Nunca vi algo assim antes!",
    "Que reviravolta inesperada!",
    "Minha mente está explodindo de surpresa!"
]


class Posts:
    def __init__(self, quantidade_user, quantidade_rede_social):
        """
        :param quantidade_user: quantidade de usuários que terá no BD
        :param quantidade_rede_social: quantidade de redes sociais no BD
        """
        ano = randint(2020, 2023)
        mes = randint(1, 12)
        if mes == 12:
            dias_no_mes = 31  # Dezembro sempre tem 31 dias
        else:
            # Verifique quantos dias há no mês gerado
            dias_no_mes = (date(ano, mes + 1, 1) - date(ano, mes, 1)).days
        dias = randint(1, dias_no_mes)  # gerando um dia aleatório com base no mês
        self.id_rede_social = randint(1, quantidade_rede_social)  # Id da rede social aleatório baseado na quantidade de redes sociais
        self.id_user = randint(1, quantidade_user)  # Id do usuário aleatório baseado na quantidade de usuários
        self.conteudo = cc(conteudo)  # Conteúdo do post aleatório
        self.data_post = date(ano, mes, dias)  # Gerando a data


def gerar_redes_sociais(quantidade_redes_sociais):
    """
    :param quantidade_redes_sociais: Quantidade de redes sociais que serão geradas no BD
    :return: DataFrame com os dados gerados
    """
    redes_sociais = [  # Nomes das redes sociais
        "SociaLink",
        "AmigoConnect",
        "InstaRede"
    ]
    dados = {"Nome": []}  # ESTRUTURA DOS DADOS
    df = pd.DataFrame(dados)  # TRANSFORMANDO A ESTRUTURA EM UM DATASET
    linhas = []
    for i in range(0, quantidade_redes_sociais):
        new_dados = {
            "Nome": redes_sociais[i]
        }
        linhas.append(new_dados)  # ADICIONANDO O DICT COM OS DADOS Á LISTA DE LINHAS
    df = pd.concat([df, pd.DataFrame(linhas)], ignore_index=True)  # JUNTANDO OS DOIS DFS
    return df


def gerar_usuarios(quantidade_user, quantidade_grupo):
    """
    :param quantidade_user: Quantidade de usuários a ser gerado no BD
    :param quantidade_grupo: Quantidade de grupos a ser gerado no BD
    :return: DataFrame com os dados gerados
    """
    dados_clientes = {  # ESTRUTURA DOS DADOS
        "nome": [],
        "email": [],
        "tel": [],
        "id_gp": []
    }
    df = pd.DataFrame(dados_clientes)  # TRANSFORMANDO A ESTRUTURA EM UM DATASET
    linhas = []
    for user in range(1, quantidade_user + 1):
        user1 = Usuarios(quantidade_grupo)
        new_dados = {
            "nome": user1.nome,
            "email": user1.email,
            "tel": user1.telefone,
            "id_gp": user1.id_grupo
        }
        linhas.append(new_dados)  # ADICIONANDO O DICT COM OS DADOS Á LISTA DE LINHAS
    df = pd.concat([df, pd.DataFrame(linhas)], ignore_index=True)  # JUNTANDO OS DOIS DFS
    return df


def gerar_post(quantidade_posts, quantidade_user, quantidade_redes_sociais):
    """
    :param quantidade_posts: Quantidade de posts a ser gerado no BD
    :param quantidade_user: Quantidade de usuários a ser gerado no BD
    :param quantidade_redes_sociais: Quantidade de redes sociais a ser gerado no BD
    :return: DataFrame com os dados gerados
    """
    dados_posts = {  # ESTRUTURA DOS DADOS
        "id_user": [],
        "conteudo": [],
        "data_post": [],
        "id_rede_social": []
    }
    df = pd.DataFrame(dados_posts)  # TRANSFORMANDO A ESTRUTURA EM UM DATASET
    linhas = []
    for post in range(1, quantidade_posts + 1):
        post1 = Posts(quantidade_user, quantidade_redes_sociais)
        new_dados = {
            "id_user": post1.id_user,
            "conteudo": post1.conteudo,
            "data post": post1.data_post,
            "id_rede_social": post1.id_rede_social
        }
        linhas.append(new_dados)  # ADICIONANDO O DICT COM OS DADOS Á LISTA DE LINHAS
    df = pd.concat([df, pd.DataFrame(linhas)], ignore_index=True)  # JUNTANDO OS DOIS DFS
    return df


def gerar_grupos(quantidade_grupo):
    """
    :param quantidade_grupo: quantidade de grupos a ser gerada
    :return: um dataframe com os grupos
    """
    global chave
    temas_com_descricao = {
        "Fotografia": "Compartilhe e discuta fotos incríveis, dicas de fotografia e técnicas de edição.",
        "Viagens": "Descubra destinos emocionantes, planeje aventuras e compartilhe suas experiências de viagem.",
        "Alimentação": "Converse sobre receitas deliciosas, dicas de culinária e nutrição saudável.",
        "Tecnologia": "Explore as últimas tendências tecnológicas, gadgets e novidades do mundo da tecnologia.",
        "Música": "Compartilhe suas músicas favoritas, artistas e discuta os últimos lançamentos musicais.",
        "Esportes": "Apaixonados por esportes podem debater sobre seus times, eventos esportivos e treinamento físico.",
        "Moda": "Converse sobre tendências de moda, estilo pessoal e dicas de beleza.",
        "Cinema": "Discuta filmes, diretores, atores e as últimas estreias do mundo do cinema.",
        "Livros": "Compartilhe suas leituras atuais, resenhas e recomendações de livros.",
        "Artesanato": "Mostre suas criações artesanais, compartilhe tutoriais e inspire-se na arte feita à mão."
    }
    dados_grupo = {  # ESTRUTURA DOS DADOS
        "Nome": [],
        "Descrição": []
    }
    df = pd.DataFrame(dados_grupo)  # TRANSFORMANDO A ESTRUTURA EM UM DATASET
    linhas = []  # ONDE SERÃO ARMAZENADO AS LINHAS DO DF
    chaves = []  # armazenando as chaves do dicionarios para poder acessar por indice
    for chave in temas_com_descricao.keys():  # PEGANDO OS TEMAS
        chaves.append(chave)
    for i in range(0, quantidade_grupo):
        new_dados = {
            "Nome": chaves[i],
            "Descrição": temas_com_descricao[chaves[i]]  # PEGANDO AS DESCRIÇÕES DE ACORDO COM O TEMA
        }
        linhas.append(new_dados)  # ADICIONANDO O DICT COM OS DADOS Á LISTA DE LINHAS
    df = pd.concat([df, pd.DataFrame(linhas)], ignore_index=True)  # JUNTANDO OS DOIS DFS
    return df
