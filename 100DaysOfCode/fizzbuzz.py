print("""
      
            ███████╗██╗███████╗███████╗██████╗ ██╗   ██╗███████╗███████╗
            ██╔════╝██║╚══███╔╝╚══███╔╝██╔══██╗██║   ██║╚══█╗██╔╝╚══███╔╝
            █████╗  ██║  ███╔╝   ███╔╝ ██████╔╝██║   ██║  ███╔╝   ███╔╝ 
            ██╔══╝  ██║ ███╔╝   ███╔╝  ██╔══██╗██║   ██║ ███╔╝   ███╔╝  
            ██║     ██║███████╗███████╗██████╔╝╚██████╔╝███████╗███████
            ╚═╝     ╚═╝╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                            
""")
  
  
  
  
n = int(input("Digite um número: "))  
    
count = 0 
for each_number in range(1,n+1):
    count = each_number
    if count % 5 == 0 and count % 3 == 0:
      print("FizzBuzz")    
        
    elif count % 5 == 0:
      print("Buzz")
        
    elif count % 3 == 0:
      print("Fizz")
    else:
      print(count)    

input("Pressione Enter para sair...")
