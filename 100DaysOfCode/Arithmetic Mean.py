print("""
 █████╗ ██████╗ ██╗████████╗██╗  ██╗███╗   ███╗███████╗████████╗██╗ ██████╗   
██╔══██╗██╔══██╗██║╚══██╔══╝██║  ██║████╗ ████║██╔════╝╚══██╔══╝██║██╔════╝   
███████║██████╔╝██║   ██║   ███████║██╔████╔██║█████╗     ██║   ██║██║       
██╔══██║██╔══██╗██║   ██║   ██╔══██║██║╚██╔╝██║██╔══╝     ██║   ██║██║       
██║  ██║██║  ██║██║   ██║   ██║  ██║██║ ╚═╝ ██║███████╗   ██║   ██║╚██████╗  
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝  


                ███╗   ███╗███████╗ █████╗ ███╗   ██╗
                ████╗ ████║██╔════╝██╔══██╗████╗  ██║
                ██╔████╔██║█████╗  ███████║██╔██╗ ██║
                ██║╚██╔╝██║██╔══╝  ██╔══██║██║╚██╗██║
                ██║ ╚═╝ ██║███████╗██║  ██║██║ ╚████║
                ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
""")

from math import ceil
# 📌 1 converter a lista de string para int
lista_das_distâncias = input("Inserir a lista de dados: ").split()
for n in range(0, len(lista_das_distâncias)):
    lista_das_distâncias[n] = int(lista_das_distâncias[n])
# converte a lista originalmente de string para int

# 📌 2 somar as distâncias
suma_das_distâncias = 0
for n in lista_das_distâncias:
    suma_das_distâncias += n

# 📌 3 contar o tamanho da lista
tamanho_da_lista = 0
for tamanho in lista_das_distâncias:
    tamanho_da_lista += 1
    
# 📌 4 Calcule a média
média_aritmética = suma_das_distâncias / tamanho_da_lista
print(f"A Média Aritmética é = {ceil(média_aritmética)}")

