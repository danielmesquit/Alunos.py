CREATE DATABASE escola;

USE escola;

CREATE TABLE alunos(
	matricula INT NOT NULL UNIQUE,
    nome VARCHAR(150) NOT NULL,
    idade INT NOT NULL,
    curso VARCHAR(150) NOT NULL,
    nota FLOAT DEFAULT 0
);

DESCRIBE alunos;

SELECT * FROM alunos;





