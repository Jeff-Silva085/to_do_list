from dados import tasks
import os

cont = 0
numberlist = 0

while cont == 0:

    #Mostrar a lista de tarefas
    print("Sua lista de tarefas:")
    print("--------------------------------------------")
    for key, value in tasks.items():
            print(f"{key}: {value}")
    print("--------------------------------------------")
    escolha = input("[1] Adicionar item\n[2] Remover um item\n-> ")
    os.system("cls")

    #-- opções da lista de tarefas --
    #   1 Adicionar nova tarefa
    if escolha == "1":
       novaTarefa = input("Qual tarefa deseja adicionar hoje?: ")
       numberlist += 1
       tasks[f"{numberlist}"] = novaTarefa
       os.system("cls") 
    
    #   2 Remover uma tarefa
    elif escolha == "2":
        if bool(tasks) == False:
             print("Não há itens na sua lista para remover")
        else:
            for key, value in tasks.items():
                print(f"{key}: {value}")
                apg = input("Digite o numero da tarefa: ")
                del tasks[apg]
                os.system("cls")    

        #print(key)
        #contador = key
        #print("Este aqui é o contador {}".format(contador))
cont = 1

#novaTarefa = input("Qual tarefa deseja adicionar hoje?: ")


#t.tasks["Tarefa 3"] = novaTarefa
#print(t.tasks["Tarefa 3"])
#print(t.tasks["tarefa 1"])