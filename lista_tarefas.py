class Lista:

    # Criação do construtor da classe.

    def __init__(self):
        self.listaTarefas = {}

    # Método para adicionar tarefa na lista.

    def adicionarTarefa(self, tarefaNova):
        nova = str(tarefaNova).capitalize()
        if len(nova) <= 30:
            self.listaTarefas[nova]='Em andamento'
            print(f'Tarefa adicionada com sucesso!')
        else:
            print('Limite de 30 caracteres foi excedido.')
        
    # Método para excluir tarefa da lista.

    def excluirTarefa(self, tarefaExcluir):
        excluir = str(tarefaExcluir).capitalize()
        if excluir in self.listaTarefas:
            self.listaTarefas.pop(excluir)
            print(f'Tarefa removida com sucesso!')
        else:
            print('Tarefa não encontrada.')

    # Método para mostrar a lista de tarefas.

    def mostrarTarefa(self):
        print(f'+{"-"*44}+')
        print(f'| {"Tarefa".ljust(28)}| Status       |')
        print(f'+{"-"*44}+')
        for i in self.listaTarefas:
            print(f'| {str(i).ljust(28)}| {str(self.listaTarefas[i]).ljust(13)}|')
        print(f'+{"-"*44}+')
    
    # Método para alternar status das tarefas entre "Em andamento" e "Conluída".

    def alterarStatus(self, tarefaExiste):
        existe = str(tarefaExiste).capitalize()
        if existe in self.listaTarefas:
            if self.listaTarefas[existe] == 'Em andamento':
                self.listaTarefas[existe] = 'Concluída'
                print(f'Status de "{existe}" alterado para "Concluída"!')
            else:
                self.listaTarefas[existe] = 'Em andamento'
                print(f'Status de "{existe}" alterado para "Em andamento"!')
        else:
            print('Tarefa não encontrada.')

    # Método para editar nome de uma tarefa existente.

    def editarTarefa(self, tarefaExistente):
        existente = str(tarefaExistente).capitalize()
        if existente in self.listaTarefas:
            perguntaDois = input('Insira o novo nome da tarefa: ')
            nova = str(perguntaDois).capitalize()
            if len(nova) <= 30:
                self.listaTarefas[nova] = self.listaTarefas.pop(existente)
                print(f'A tarefa "{existente}" foi alterada para "{nova}".')
            else:
                print('Limite de 30 caracteres foi excedido.')    
        else:
            print('Tarefa não encontrada.')