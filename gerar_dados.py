from random import choice as cc
from random import randint

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
        self.telefone = str(randint(90000, 99999)) + "-" + str(randint(1111, 9999))
        self.id_grupo = randint(1, quantidade_grupos)



