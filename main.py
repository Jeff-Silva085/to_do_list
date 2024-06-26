from dados import tasks
import os

cont = 0

while cont == 0:
    #Mostrar a lista de tarefas
    for key, value in tasks.items():
            print(f"{key}: {value}")

    escolha = input("[1] Adicionar item\n[2] Remover um item\n[3] Ver a lista de tarefas")

    #-- opções da lista de tarefas --
    #   1 Adicionar nova tarefa
    if escolha == "1":
       novaTarefa = input("Qual tarefa deseja adicionar hoje?: ")
       tasks["3".format] = novaTarefa 
    
    #   2 Remover uma tarefa
    elif escolha == "2":
        for key, value in tasks.items():
            print(f"{key}: {value}")

        apg = input("Digite o numero da tarefa: ")
        del tasks[apg]
            

        #print(key)
        #contador = key
        #print("Este aqui é o contador {}".format(contador))
cont = 1

#novaTarefa = input("Qual tarefa deseja adicionar hoje?: ")


#t.tasks["Tarefa 3"] = novaTarefa
#print(t.tasks["Tarefa 3"])
#print(t.tasks["tarefa 1"])