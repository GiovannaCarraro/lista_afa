from classe_tarefa import Tarefa

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
   
  elif tarefa == 2:
    print("Você escolheu listar tarefas")
      
  elif tarefa == 3:
    print("Você escolheu marcar concluido")
        
  elif tarefa == 4:
    print("Você escolheu remover tarefa")

  elif tarefa == 5:
    print("Você escolheu sair")
        
  break
    
    