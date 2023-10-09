from random import choice as cc
from random import randint
from datetime import date

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
        primeiro_nome = cc(nomes)
        sobrenome = cc(sobrenomes)
        self.nome = primeiro_nome + " " + sobrenome
        self.email = primeiro_nome.lower() + sobrenome.lower() + cc(emails)
        self.telefone = str(randint(90000, 99999)) + "-" + str(randint(1000, 9999))
        self.id_grupo = randint(1, quantidade_grupos)


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
    def __init__(self, quantidade_user):
        ano = randint(2000, 2023)
        mes = randint(1, 12)
        if mes == 12:
            dias_no_mes = 31  # Dezembro sempre tem 31 dias
        else:
            # Verifique quantos dias há no mês gerado
            dias_no_mes = (date(ano, mes + 1, 1) - date(ano, mes, 1)).days
        dias = randint(1, dias_no_mes)
        self.id_rede_social = randint(1, 3)
        self.id_user = randint(1, quantidade_user)
        self.conteudo = cc(conteudo)
        self.data_post = date(ano, mes, dias)


# grupos
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


class Grupos:
    def __init__(self):
        escolhido = randint(0, 9)
        tema = list(temas_com_descricao.keys())[escolhido]
        descricao = temas_com_descricao[tema]
        self.nome = tema
        self.descricao = descricao


# redes sociais
redes_sociais = [
    "SociaLink",
    "AmigoConect",
    "InstaRede"
]


class RedeSocial:
    def __init__(self):
        self.nome = cc(redes_sociais)
