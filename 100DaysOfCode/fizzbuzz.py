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
# # se o número for divível por 5 e 3, serão múltiplos dos mesmos.
    if count % 5 == 0 and count % 3 == 0:
      print("FizzBuzz")     
    # checar se a variável "count" é divisível por 5 e 3(true): printar'FizzBuzz'
      
    elif count % 5 == 0:
    #checar se a variável é divisível por 5
    # se for(true), print(buzz) 
      print("Buzz")
        
    elif count % 3 == 0:
      print("Fizz")
    # checar se a variável é divísivel por 3
    # se for(true): print("Fizz")
    
    else:
      print(count)    
    # caso tudo não for satisfeito, print o número na variável.
    
input("Pressione Enter para sair...")
