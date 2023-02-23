"""
📃 Documentação

🔑 Script para gerar senhas com base em critérios do usuário.

Algoritimo usado para selecionar itens de lista, randomizalos e colocá-los em ordem.

Cria-se uma variável str vazia que irá armazenar os itens,
em seguida, o uso do for loop para itenizar a quantidade de vezes que tudo vai acontecer para a variável i,
logo depois, dentro do bloco de execução do loop,
i recebe a randomização de um dos valores da variável "letters"
por conseguinte, a variável vazia recebe o valor dela mesma + o valor de i
tantas vezes quanto foi especificado no range
resultando na selecão da quantidade de caracteres randomicos especificado no input.
por fim, os resultados dos loops são printados em ordem para o usuário.

Em suma, o algoritmo é pensado para gerar senhas aleatórias com base nos critérios do usuário.
    
OPS: o valor da variável letters_char não é subscrito no loop pelo seguinte:
a variável começa vazia, recebe um valor X, na próxima itenização recebe X e Y, na seguinte, X,Y e Z
até o fim da itenização especificado no range. 
    
"""
#Password Generator Project
 
# # Easy Level - Order of characters not randomised:
# # e.g. 4 letter, 2 symbol, 2 number = sfga#$12

# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# print("Bem vindo ao PyPassword Generator!")
# nr_letters = int(input("Quantas letras você gostaria de ter na senha?\n")) 
# nr_symbols = int(input(f"Quantos símbolos você prefere?\n"))
# nr_numbers = int(input(f"Quantos números você quer?\n"))

# # variável letters_char é uma str vazia
# random_letters = ""
# # para variável i no intervalo de 0 ao número do input
# for i in range(0,nr_letters):
# # i recebe uma randomização dos valores da variável (letters)
#     i = random.choice(letters)
# # a variável letters_char recebe o valor dela mesma (vazio) mais o valor de i
#     random_letters += i

# random_symbols = ""
# for n in range(0,nr_symbols):
#     n = random.choice(symbols)
#     random_symbols += n

# random_numbers = ""
# for z in range(0,nr_numbers):
#     z = random.choice(numbers)
#     random_numbers += z

# print("Sua senha é:",random_letters + random_symbols + random_numbers)

# # Hard Level - Order of characters randomised:
# # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Bem vindo ao PyPassword Generator!")
nr_letters = int(input("Quantas letras você gostaria de ter na senha?\n")) 
nr_symbols = int(input(f"Quantos símbolos você prefere?\n"))
nr_numbers = int(input(f"Quantos números você quer?\n"))

random_letters = ""

for i in range(0,nr_letters):

    i = random.choice(letters)

    random_letters += i

random_symbols = ""
for n in range(0,nr_symbols):
    n = random.choice(symbols)
    random_symbols += n

random_numbers = ""
for z in range(0,nr_numbers):
    z = random.choice(numbers)
    random_numbers += z
    
random_order = [random_letters, random_symbols, random_numbers]
random.shuffle(random_order)

no_space = ''

password = no_space.join(random_order)

print("Sua senha é:",password)