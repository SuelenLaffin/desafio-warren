

# Traz uma lista de números de 10 a 1000, somando esses números com o seu reverso
# traz apenas os resultados ímpares dessa soma.

def my_num(numero):
        return numero[::-1] # função para tornar o número inverso

for x in range(10, 1000): #percorrer uma lista de 10 até 1000
    reverso = my_num(str(x))

    if reverso[0] !='0': # se o reverso começar com 0, remover da lista
        soma = int(x) + int(reverso)

        if soma % 2 == 1 and x != 0:
            print(str(x) + ' + ' + str(reverso) + ' = ' + str(soma)) # somando o numero com o seu reverso e exibindo somente os ímpares





















# print('****NUMEROS TOTAIS 1****')

# listaNormal = range(11,1000)

# for x in listaNormal:
#     print(x)


# num = [(int(input('Digite um valor inteiro positivo: '))) for c in range(10)]

# print(num)

# num_reverso = int(input('digite um número: '))
# reverse_num = 0
# while(num_reverso > 0):
#     Reminder = num_reverso%10
#     reverse_num = (reverse_num *10) + Reminder
#     num_reverso = num_reverso //10
#     print("Os números reversos são: %d" %reverse_num)



















# def ListaNumImpar(number):
#     if number%2==1:
#         print ("Números Ímpares:",(number))
    
# a = range(11,1000)

# for item in a:
#     ListaNumImpar(item)

# soma = list(map(lambda v1, v2 : v1 + v2, listaNumTotal1, listaNumTotal2))


# print('-----------------------------------------------------------------------------------------------------------------')


# print('-----------------------------------------------------------------------------------------------------------------')

# soma = list(map(lambda v1, v2 : v1 + v2, listaNumTotal1, listaNumTotal2))


# for x in soma:
#     if(x % 2 ==1):
#         impares = x
#         print(impares)


        


# def contaImpares(listaImpares):
    
    
#     impares = 0

#     for num in soma:
#         if (num % 2 == 0):
#             return  impares

# listaImpares=list()
# print(contaImpares(listaImpares))




    







# lista_reversa = list(listaNumTotal) 

# def InverterNum():
#     reverter =[]
#     reverter.extend(lista_reversa)
#     reverter.reverse()

#     revertido = str(reverter).strip('[]')
    

#     return revertido

# ver = list(print(InverterNum()))