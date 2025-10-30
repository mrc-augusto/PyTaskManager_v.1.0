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
    status = 'Concluída' if tarefa['completa'] else 'Pendente'
    nome_tarefa = tarefa['tarefa']
    print(f'{indice}. {nome_tarefa} - [{status}]')

tarefas = []

while True:
  print('\nMenu de Gerenciador de Lista de Tarefas:')
  print('1. Adicionar Tarefa')
  print('2. Ver Tarefas')
  print('3. Atualizar Tarefa')
  print('4. Completar Tarefa')
  print('5. Deletar Tarefas completadas') 
  print('6. Sair')
  

  escolha = input('Digite o número da opção desejada: ')

  if escolha == '1':
    nome_tarefa = input('Digite o nome da tarefa: ')
    adicionar_tarefa(tarefas, nome_tarefa)

  elif escolha == '2':
    ver_tarefas(tarefas)

  elif escolha == '6':
    break

print('Encerrando o gerenciador de tarefas. Até logo!')