while True:
  print('\nMenu de Gerenciador de Lista de Tarefas:')
  print('1. Adicionar Tarefa')
  print('2. Ver Tarefas')
  print('3. Atualizar Tarefa')
  print('4. Completar Tarefa')
  print('5. Deletar Tarefas completadas')
  print('6. Sair')
  

  escolha = input('Digite o número da opção desejada: ')

  if escolha == '6':
    break

print('Encerrando o gerenciador de tarefas. Até logo!')