from time import sleep
from lista_tarefas import Lista

# Faz a instância da classe Lista.

listaTarefas = Lista()

# Código para fazer a escolha de alternativas.

flag = True

while flag:
    print('''
O que deseja fazer?
          
1 - Adicionar tarefa.
2 - Excluir tarefa.
3 - Alterar status.
4 - Editar tarefa.
5 - Mostrar lista de tarefas.
6 - Sair.
''')
    
    # Analisa todas as alternativas do 1 ao 6 e retorna suas funcionalidades.


    pergunta = input('--> ')
    if pergunta == '1':
        perguntaUm = input('Insira o nome da tarefa: ')
        print(' ')
        sleep(0.5)
        listaTarefas.adicionarTarefa(perguntaUm)
        sleep(0.75)
    elif pergunta == '2':
        listaTarefas.mostrarTarefa()
        perguntaUm = input('Insira o nome da tarefa que deseja excluir: ')
        print(' ')
        sleep(0.5)
        listaTarefas.excluirTarefa(perguntaUm)
        sleep(0.75)
    elif pergunta == '3':
        listaTarefas.mostrarTarefa()
        perguntaUm = input('Insira a tarefa que deseja trocar o status: ')
        print(' ')
        sleep(0.5)
        listaTarefas.alterarStatus(perguntaUm)
        sleep(0.75)
    elif pergunta == '4':
        listaTarefas.mostrarTarefa()
        perguntaUm = input('Insira a tarefa que deseja editar: ')
        print(' ')
        sleep(0.5)
        listaTarefas.editarTarefa(perguntaUm)
        sleep(0.75)
    elif pergunta == '5':
        print(' ')
        sleep(0.5)
        listaTarefas.mostrarTarefa()
        sleep(0.75)
    elif pergunta == '6':
        sleep(0.5)
        print('\nVocê escolheu sair.')
        sleep(0.75)
        break
    else:
        sleep(0.5)
        print('\nEsta opção não existe.')
        sleep(0.75)