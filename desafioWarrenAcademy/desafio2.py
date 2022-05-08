

qtde_alunos_classe = int(input('Quantidade de alunos na classe: ')) # o usuário digitará a quantidade de alunos na classe

print('Atrasados = -1,-2(minutos), horário normal = 1') # aqui uma dica para colocarem o tempo de chegada, chegou 1 minuto atrasado, digite -1, chegou 2 minutos adiantado, digite 2.

tempoChegada = [int(input('Tempo de chegada:')) for x in range(qtde_alunos_classe)]
print(tempoChegada) # o tempo de chegada levará em consideração quantos alunos tem na classe. Se tiver 4, pedirá o tempo de chegada dos 4.

atrasados = 0


for i in range(0,len(tempoChegada)): #percorre a lista dos alunos para contabilizar os atrasados.
    if tempoChegada[i] < 0:
        atrasados = atrasados +1
    
if atrasados >=3: # se o número de alunos atrasados for maior ou igual a 3, a aula é cancelada.
    print('Aula Cancelada')
else:
    print('Aula Normal')
  





# def AulaNormal():
#     for i in qtde_alunos_atrasados:
#         if i >= 3:
#             for c in minutos_atrasados:
#                 if c >=0:
#                     print('AULA NORMAL!!!')

# print(AulaNormal())