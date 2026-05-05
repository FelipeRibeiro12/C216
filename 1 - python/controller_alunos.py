from aluno import Aluno

class ControllerAlunos:
    def __init__(self):
        self.alunos = {}
        self.contadores_curso = {}

    def _gerar_matricula(self, curso):
        self.contadores_curso[curso] = self.contadores_curso.get(curso, 0) + 1
        return f"{self.contadores_curso[curso]}"

    def criarAluno(self, nome: str, curso: str, email_user: str):
        cursos_validos = ['GEA', 'GEB', 'GEC', 'GEL', 'GEP', 'GES', 'GET']
        if curso not in cursos_validos:
            raise ValueError(f"Curso inválido. Escolha um dos seguintes: {', '.join(cursos_validos)}")
            
        matricula = self._gerar_matricula(curso)
        email = f"{email_user}@{curso}.inatel.br"
        novo_aluno = Aluno(nome, email, curso, matricula)
        self.alunos[matricula] = novo_aluno
        return novo_aluno

    def listarAlunos(self):
        return list(self.alunos.values())
        
    def getAluno(self, matricula: str):
        return self.alunos.get(matricula)

    def atualizarAluno(self, matricula: str, nome: str = None, curso: str = None, email_user: str = None):
        aluno = self.alunos.get(matricula)
        if not aluno:
            return None
        
        if nome:
            aluno.nome = nome
        if curso:
            cursos_validos = ['GEA', 'GEB', 'GEC', 'GEL', 'GEP', 'GES', 'GET']
            if curso not in cursos_validos:
                raise ValueError(f"Curso inválido. Escolha um dos seguintes: {', '.join(cursos_validos)}")
            aluno.curso = curso
        if email_user:
            aluno.email = f"{email_user}@{aluno.curso}.inatel.br"
            
        return aluno

    def deletarAluno(self, matricula: str):
        return self.alunos.pop(matricula, None)
