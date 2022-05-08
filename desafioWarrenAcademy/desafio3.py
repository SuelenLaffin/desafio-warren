num = int(input('Digite um número  maior que 10: ')) # input para que seja digitado um número

if num >10:
    vetor = []

    for i in range(0,3):
        vetor.append(int(input('Digite os valores no vetor:'))) # for para digitar três valores e eles são inseridos em uma lista.
    print(vetor)

    somaLista = sum(vetor)
    print(f'A soma dos valores do vetor é: {somaLista}') #soma dhttps://github.com/SuelenLaffin/desafio-warren.gitos números dentro da lista
else:
    print('Valor inválido! Digite um valor maior que 10!')

