print("""
      
            ███████╗██╗███████╗███████╗██████╗ ██╗   ██╗███████╗███████╗
            ██╔════╝██║╚══███╔╝╚══███╔╝██╔══██╗██║   ██║╚══█╗██╔╝╚══███╔╝
            █████╗  ██║  ███╔╝   ███╔╝ ██████╔╝██║   ██║  ███╔╝   ███╔╝ 
            ██╔══╝  ██║ ███╔╝   ███╔╝  ██╔══██╗██║   ██║ ███╔╝   ███╔╝  
            ██║     ██║███████╗███████╗██████╔╝╚██████╔╝███████╗███████
            ╚═╝     ╚═╝╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                            
""")
  
  
  
# entrada do usuário
n = int(input("Digite um número: "))  

# contagem de números    
count = 0 
for each_number in range(1,n+1):
    count = each_number

# checar condições
    if count % 5 == 0 and count % 3 == 0:
      print("FizzBuzz")    
      # se o número for divisível por 5 e 3, print'fizzBuzz'.
      # objetivo é iterar todos os múltiplos de 5 e 3      
      
    elif count % 5 == 0:
      print("Buzz")
        
    elif count % 3 == 0:
      print("Fizz")
    else:
      print(count)    

input("Pressione Enter para sair...")
