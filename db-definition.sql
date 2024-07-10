create database if not exists notas;
use notas;
drop table if exists notas;


create table if not exists notas (
	id int not null auto_increment,
    nombre varchar(255),
    asunto varchar(255),
    nota varchar(5000),
    primary key (id)
);

-- insert into notas (nombre, asunto, nota) values('Test', 'test', 'nota test');

-- select * from enotas;