# from classe_tarefa import Tarefa
afazeres = []
while True:
  #Menu principal
    print("""     _____  
          /  ___  \\
        /  /  _  \  \\
      /( /( /(_)\ )\ )\\
    (  \  \ ___ /  /  )
    (    \ _____ /    )
    /(               )\\
    |  \             /  |
    |    \ _______ /    |
    \    / \   / \    /
      \/    | |    \/
            | | 
            | |
            | |
          
    LISTA DE AFAZERES
        1- INSERIR TAREFAS
        2- LISTAR TAREFAS
        3- MARCAR COMO CONCLUIDO
        4- REMOVER TAREFA
        5- SAIR
          """)
        
    tarefa = int(input("Escolha o que deseja realizar:"))
    
    if tarefa == 1:
      print("Você escolheu inserir tarefas") 
      tarefa_adc = input("Qual tarefa deseja adicionar?")
      afazeres.append(tarefa_adc)
      
    elif tarefa == 2:
      print("Você escolheu listar tarefas")
      for tarefa in afazeres:
        print(tarefa)
                            
    elif tarefa == 3:
      print("Você escolheu marcar concluido")     
      numero = 0
      for tarefa in afazeres:
        print(f"{numero} {tarefa}")
        numero += 1
        concluido = int(input("Qual das tarefas você quer marcar como concluida:"))
        afazeres[concluido] = afazeres [concluido] + "✔"

    elif tarefa == 4:
      print("Você escolheu remover tarefa")
      remover = int(input("Qual item você deseja remover?"))
      afazeres.remove(remover)

    elif tarefa == 5:
      print("Você escolheu sair")
      break
    
      
    