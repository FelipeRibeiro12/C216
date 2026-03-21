class Aluno:
    def __init__(self, nome, email, curso, matricula):
        self.nome = nome
        self.email = email
        self.curso = curso
        self.matricula = matricula

    def __str__(self):
        return f"nome: {self.nome}, email: {self.email}, matricula: {self.matricula} {self.curso}"
