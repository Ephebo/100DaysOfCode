print("""
           
████████╗██████╗ ███████╗ █████╗ ███████╗██╗   ██╗██████╗ ███████╗    ███╗   ███╗ █████╗ ██████╗ 
╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝    ████╗ ████║██╔══██╗██╔══██╗
   ██║   ██████╔╝█████╗  ███████║███████╗██║   ██║██████╔╝█████╗      ██╔████╔██║███████║██████╔╝
   ██║   ██╔══██╗██╔══╝  ██╔══██║╚════██║██║   ██║██╔══██╗██╔══╝      ██║╚██╔╝██║██╔══██║██╔═══╝ 
   ██║   ██║  ██║███████╗██║  ██║███████║╚██████╔╝██║  ██║███████╗    ██║ ╚═╝ ██║██║  ██║██║     
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
        
""")

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# seleciona os inputs separadamente.
vertical_selection = int(position[0])
horizontal_selection = int(position[1])

# seleciona os elementos na lista com base no valor das variáveis
# "vertical_selection" e "horizontal_selection".
# iguala o elemento selecionado na variável map para "X", substituindo-o.
map[horizontal_selection -1][vertical_selection -1] = 'X'

print(f"{row1}\n{row2}\n{row3}")

