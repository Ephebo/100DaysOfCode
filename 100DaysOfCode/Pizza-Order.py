print("""

            ██████╗ ██╗███████╗███████╗ █████╗      ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
            ██╔══██╗██║╚══███╔╝╚══███╔╝██╔══██╗    ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
            ██████╔╝██║  ███╔╝   ███╔╝ ███████║    ██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝
            ██╔═══╝ ██║ ███╔╝   ███╔╝  ██╔══██║    ██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗
            ██║     ██║███████╗███████╗██║  ██║    ╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
            ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
""")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

S = 15
M = 20
L = 25
pepperoniSmall = 2
pepperoniMedio = 3
pepperoniLarge = 3
cheese = 1

if size == "S" and add_pepperoni == "Y" and extra_cheese == "Y":
    bill = S + pepperoniSmall + cheese
    print(f"Your final bill is: ${bill}.")
    if size == "S" and add_pepperoni == "N" and extra_cheese == "N":
        bill = S
        print(f"Your final bill is: ${bill}.")
    else:
        bill = S + pepperoniSmall
        print(f"Your final bill is: ${bill}.")

elif size == "M" and add_pepperoni == "Y" and extra_cheese == "Y":
    bill = M + pepperoniMedio + cheese
    print(f"Your final bill is: ${bill}.")
elif size == "M" and add_pepperoni == "N" and extra_cheese == "N":
    bill = M
    print(f"Your final bill is: ${bill}.")
elif size == "M" and add_pepperoni == "Y" and extra_cheese == "N":
    bill = M + pepperoniMedio
    print(f"Your final bill is: ${bill}.")
elif size == "M" and add_pepperoni == "N" and extra_cheese == "Y":
    bill = M + cheese
    print(f"Your final bill is: ${bill}.")


elif size == "L" and add_pepperoni == "Y" and extra_cheese == "Y":
    bill = L + pepperoniLarge + cheese
    print(f"Your final bill is: ${bill}.")
elif size == "L" and add_pepperoni == "N" and extra_cheese == "N":
    bill = L
    print(f"Your final bill is: ${bill}.")
elif size == "L" and add_pepperoni == "Y" and extra_cheese == "N":
    bill = L + pepperoniLarge
    print(f"Your final bill is: ${bill}.")
elif size == "L" and add_pepperoni == "N" and extra_cheese == "Y":
    bill = L + cheese
    print(f"Your final bill is: ${bill}.")
else:
    bill = S + cheese
    print(f"Your final bill is: ${bill}.")
