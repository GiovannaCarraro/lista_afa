class Tarefa:

    def __init__(self):
        self.lista_tarefas = []

    def adicionar_tarefa(self):
        tarefa = input("Qual tarefa você deseja incluir?")
        self.lista_tarefa.append(tarefa)

    def listar_tarefa(self):
        for tarefa in self.lista_tarefas:
            print(tarefa)