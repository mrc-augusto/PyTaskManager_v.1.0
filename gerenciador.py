def adicionar_tarefa(tarefas, nome_tarefa):
  tarefa={'tarefa': nome_tarefa, 'completa': False}
  tarefas.append(tarefa)
  print (f'Tarefa {nome_tarefa} foi adicionada com sucesso!')
  return

def ver_tarefas(tarefas):
  if not tarefas:
    print('Nenhuma tarefa na lista.')
    return

  print('\nLista de Tarefas:')
  for indice, tarefa in enumerate(tarefas, start=1):
    status = '✔️' if tarefa['completa'] else ' '
    nome_tarefa = tarefa['tarefa']
    print(f'{indice}. [{status}] {nome_tarefa}')
  return

def atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
  indice_tarefa_ajustado = indice_tarefa -1
  tarefas[indice_tarefa_ajustado] ['tarefa'] = novo_nome_tarefa
  print(f'Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa} com sucesso!')
  return

def deletar_tarefas(tarefas, indice_tarefa_deletar):
  indice_tarefa_ajustado = indice_tarefa_deletar -1
  del tarefas[indice_tarefa_ajustado]
  print(f'Tarefa {indice_tarefa_deletar} - {nome_tarefa} deletada com sucesso!')
  return

tarefas = []

while True:
  print('\nMenu de Gerenciador de Lista de Tarefas:')
  print('1. Adicionar Tarefa')
  print('2. Ver Tarefas')
  print('3. Atualizar Tarefa')
  print('4. Completar Tarefa')
  print('5. Deletar Tarefas completadas') 
  print('6. Deletar Tarefa')
  print('7. Sair')
  

  escolha = input('Digite o número da opção desejada: ')

  if escolha == '1':
    nome_tarefa = input('Digite o nome da tarefa: ')
    adicionar_tarefa(tarefas, nome_tarefa)

  elif escolha == '2':
    ver_tarefas(tarefas)

  elif escolha == '3':
    ver_tarefas(tarefas)
    indice_tarefa = int(input('Digite o número da tarefa que deseja atualizar:'))
    novo_nome_tarefa = input('Digite o novo nome da tarefa: ')
    atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)

  elif escolha == '4':
    pass

  elif escolha == '5':
    pass

  elif escolha == '6':
    ver_tarefas(tarefas)
    indice_tarefa_deletar = int(input('Digite o número da tarefa que deseja deletar:'))
    deletar_tarefas(tarefas, indice_tarefa_deletar)

  elif escolha == '7':
    break

print('Encerrando o gerenciador de tarefas. Até logo!')