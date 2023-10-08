-- criando banco
create database bd_prod;
use bd_prod;

-- criando tabelas
create table if not exists usuarios (
    id int auto_increment primary key,
    id_grupo int,
    nome varchar(100),
    email varchar(100),
    telefone varchar(20),
    FOREIGN KEY (id_grupo) REFERENCES grupos(id)
);
create table if not exists posts (
	id int auto_increment primary key,
    data_post datetime,
	conteudo text,
    id_user int,
	FOREIGN KEY (id_user) REFERENCES usuarios(id)
);
create table if not exists grupos (
	id int auto_increment primary key,
    id_user int,
    nome varchar(255),
    descricao varchar(255),
	FOREIGN KEY (id_user) REFERENCES usuarios(id)
);

