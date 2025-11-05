def adicionar_tarefa(tarefas, nome_tarefa):
  tarefa={'tarefa': nome_tarefa, 'completa': False}
  tarefas.append(tarefa)
  print (f'Tarefa {nome_tarefa} foi adicionada com sucesso!')

def ver_tarefas(tarefas):
  if not tarefas:
    print('Nenhuma tarefa na lista.')
    return

  print('\nLista de Tarefas:')
  for indice, tarefa in enumerate(tarefas, start=1):
    status = ' ✓ ' if tarefa['completa'] else ' X '
    nome_tarefa = tarefa['tarefa']
    print(f'{indice}. [{status}] {nome_tarefa}')

def atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
  indice_tarefa_ajustado = indice_tarefa -1

  if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
    tarefas[indice_tarefa_ajustado] ['tarefa'] = novo_nome_tarefa
    print(f'Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa} com sucesso!')
  else:
    print('Índice inválido.')

def deletar_tarefa(tarefas, indice_tarefa_deletar):
  indice_tarefa_ajustado = indice_tarefa_deletar -1
  if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
    del tarefas[indice_tarefa_ajustado]
    print(f'Tarefa {indice_tarefa_deletar} deletada com sucesso!')
  else:
    print('Tarefa não encontrada.')

def deletar_tarefa_completada(tarefas):
  for tarefa in tarefas:
    if tarefa['completa']:
      tarefas.remove(tarefa)
      print('Tarefa completada deletada com sucesso!')
    return
  print('Não há tarefa completada para deletar.')

def tarefa_completada(tarefas, completar_tarefa):
  indice_tarefa_ajustado = completar_tarefa -1

  if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
    tarefas[indice_tarefa_ajustado]['completa'] = True
    print(f'Tarefa {completar_tarefa} marcada como completa!')
  else:
    print('Tarefa não encontrada.')
  

tarefas = []

while True:
  print('\nMenu de Gerenciador de Lista de Tarefas:')
  print('1. Adicionar Tarefa')
  print('2. Ver Tarefas')
  print('3. Atualizar Tarefa')
  print('4. Completar Tarefa')
  print('5. Deletar Tarefa')
  print('6. Deletar Tarefa Completada')
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
    ver_tarefas(tarefas)

  elif escolha == '4':
    ver_tarefas(tarefas)
    completar_tarefa = int(input('Digite o número da tarefa que deseja completar: '))
    tarefa_completada(tarefas, completar_tarefa)
    ver_tarefas(tarefas)
  
  elif escolha == '5':
    ver_tarefas(tarefas)
    indice_tarefa_deletar = int(input('Digite o número da tarefa que deseja deletar:'))
    deletar_tarefa(tarefas, indice_tarefa_deletar)
    ver_tarefas(tarefas)

  elif escolha == '6':
    ver_tarefas(tarefas)
    deletar_tarefa_completada(tarefas)
    ver_tarefas(tarefas)

  elif escolha == '7':
    break

  else:
    print('Opção inválida. Por favor, escolha uma opção existente no menu.')

print('Encerrando o gerenciador de tarefas. Até logo!')