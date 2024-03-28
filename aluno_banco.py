import pymysql.cursors
from aluno import Aluno

class AlunoBanco():

    def __init__(self, host: str,username: str,db: str,password: str):
        self.conexao = self.criarConexao(host, username, db, password)

        self.cursor = self.conexao.cursor()

    def criarConexao(self, host: str,username: str,db: str,password: str):
        try:
            conn = pymysql.connect(host=host,
                                   user=username,
                                   db=db,
                                   password=password,
                                   cursorclass=pymysql.cursors.DictCursor)
            return conn
        except Exception as erro:
            print(f"Erro ao conectar ao banco! Erro: {erro}")

    def insert(self, aluno: Aluno):
        try:
            sql = ("INSERT INTO alunos (matricula, nome , idade, curso, nota)"
                   "VALUES (%s, %s, %s, %s, %s)")
            self.cursor.execute(sql, (aluno.matricula, aluno.nome,
                                      aluno.idade, aluno.curso, aluno.nota))
            self.conexao.commit()
            return "Aluno cadastrado com sucesso!"

        except Exception as erro:
            return f"Erro ao inserir! Erro: {erro}"

    def update(self, aluno: Aluno):
        try:
            sql = ("UPDATE alunos SET nome = %s, idade = %s, curso = %s, nota = %s "
                   "WHERE matricula = %s")
            self.cursor.execute(sql, (aluno.nome, aluno.idade, aluno.curso,
                                      aluno.nota, aluno.matricula))
            self.conexao.commit()
            return "Dados alterados!"

        except Exception as erro:
            return f"Erro ao editar! Erro: {erro}"

    def delete(self, matricula: int):
        try:
            sql = "DELETE FROM alunos WHERE matricula= %s"
            self.cursor.execute(sql,matricula)
            self.conexao.commit()
            return "Dados removidos com sucesso!"

        except Exception as erro:
            return f"Erro ao remover o aluno! Erro:`{erro}"

    # def select(self) -> List or None:

    def select(self):
        try:
            sql = "SELECT * from alunos"
            self.cursor.execute(sql)
            alunos = self.cursor.fetchall() # quero exibir os dados da tabela [listagem de dados]
            return alunos

        except Exception as erro:
            return f"Erro ao listar alunos! Erro:{erro}"

if __name__ == "__main__":
    a = AlunoBanco('localhost','root',"escola","")
    aluno1 = Aluno('João',15,"Js",4.7)
    aluno2 = Aluno('Maria', 24, "React", 8.2)

    a.insert(aluno1)
    a.insert(aluno2)

    print(a.select())

    aluno1.nome="Jubiscleudo"
    a.update(aluno1)
    print(a.select())

    a.delete(aluno2.matricula)
    print(a.select())
