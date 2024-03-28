# ORM
# sql alchemy (ao criar a classe a tabela já é criada
import uuid

class Aluno:

    matricula = 0   #variável estática (pertence a classe) [controle de objetos criados]

    def __init__(self,nome: str,idade: int,curso: str,nota: float):
        Aluno.matricula += 1
        self.matricula = uuid.uuid4()
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota

    def __repr__(self):
        return (f"""Aluno {Aluno.matricula}...
        Matrícula: {self.matricula}
        Nome:{self.nome}
        Idade: {self.idade}
        Curso: {self.curso}
        Nota: {self.nota}""")

if __name__ == "__main__":
    print(Aluno('Daniel',29,"Python",9.9))
