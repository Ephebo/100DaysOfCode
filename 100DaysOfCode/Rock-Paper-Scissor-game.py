from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

all_choices = [rock,paper,scissors]


list_of_computerChoices = all_choices[randint(0,2)]


userChoices = input("Digite 0 para Pedra, 1 para Papel e 2 para Tesoura: ")
list_of_userChoices  = [rock,paper,scissors]

print("Your choice:",list_of_userChoices[int(userChoices)])
print("choice of computer: ",list_of_computerChoices)

if userChoices == "0" and list_of_computerChoices == scissors:
    print("Você ganhou!")
elif userChoices == "0" and list_of_computerChoices == paper:   
    print("Você perdeu!")
elif userChoices == "0" and list_of_computerChoices == rock:
    print("Empate!")
    
elif userChoices == "1" and list_of_computerChoices == scissors:
    print("Você Perdeu!")
elif userChoices == "1" and list_of_computerChoices == paper:   
    print("Empate!")
elif userChoices == "1" and list_of_computerChoices == rock:
    print("Você ganhou!")


elif userChoices == "2" and list_of_computerChoices == scissors:
    print("Empate!")
elif userChoices == "2" and list_of_computerChoices == paper:   
    print("Você ganhou!")
elif userChoices == "2" and list_of_computerChoices == rock:
    print("Você perdeu!")
#Write your code above this line 👆
