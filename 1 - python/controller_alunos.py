from aluno import Aluno

class ControllerAlunos:
    def __init__(self):
        self.alunos = {}
        self.contadores_curso = {}
        
    def escolher_curso(self, curso_atual=None):
        cursos_validos = ['GEA', 'GEB', 'GEC', 'GEL', 'GEP', 'GES', 'GET']
        print("Selecione o curso:")
        for idx, curso in enumerate(cursos_validos, 1):
            print(f"{idx}. {curso}")
        if curso_atual:
            prompt = f"Digite o número do curso (atual: {curso_atual}): "
        else:
            prompt = "Digite o número do curso: "
        while True:
            opcao = input(prompt)
            if opcao.isdigit() and 1 <= int(opcao) <= len(cursos_validos):
                return cursos_validos[int(opcao) - 1]
            print(f"Opção inválida. Digite um número de 1 a {len(cursos_validos)}.")

    def _gerar_matricula(self, curso):
        self.contadores_curso[curso] = self.contadores_curso.get(curso, 0) + 1
        return f"{self.contadores_curso[curso]}"

    def criarAluno(self):
        nome = input("Nome: ").strip()
        curso = self.escolher_curso()
        matricula = self._gerar_matricula(curso)
        email_user = input("Email (sem @...): ").strip()
        email = f"{email_user}@{curso}.inatel.br"
        self.alunos[matricula] = Aluno(nome, email, curso, matricula)
        print(f"Aluno {nome}, email: {email}, matricula: {matricula} {curso} foi criado")

    def listarAlunos(self):
        if not self.alunos:
            print("Nenhum aluno encontrado.")
            return
        
        for aluno in self.alunos.values():
            print(aluno)

    def atualizarAluno(self):
        matricula = input("Matricula do aluno: ").strip().upper()
        aluno = self.alunos.get(matricula)
        
        if not aluno:
            print("Aluno não encontrado.")
            return
        
        nome = input(f"Novo nome ({aluno.nome}): ").strip() or aluno.nome
        curso = self.escolher_curso(aluno.curso)
        email_user = input(f"Novo email (sem @...): ").strip() or aluno.email.split('@')[0]
        aluno.nome = nome
        aluno.curso = curso
        aluno.email = email_user + f"@{curso}.inatel.br"
        print(f"Aluno {aluno.nome}, email: {aluno.email}, matricula: {aluno.matricula} {aluno.curso} foi atualizado")

    def deletarAluno(self):
        matricula = input("Matricula do aluno: ").strip().upper()
        
        if matricula in self.alunos:
            aluno = self.alunos.pop(matricula)
            print(f"Aluno {aluno.nome}, matricula {aluno.matricula} foi deletado")
            
        else:
            print("Aluno não encontrado.")
