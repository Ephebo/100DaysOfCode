# ==================================== START ===========================================================
print(""" 
       ██████╗ ██████╗ ██████╗      █████╗ ███╗   ██╗██████╗     ███████╗██╗   ██╗███████╗███╗   ██╗
       ██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗████╗  ██║██╔══██╗    ██╔════╝██║   ██║██╔════╝████╗  ██║
       ██║   ██║██║  ██║██║  ██║    ███████║██╔██╗ ██║██║  ██║    █████╗  ██║   ██║█████╗  ██╔██╗ ██║
       ██║   ██║██║  ██║██║  ██║    ██╔══██║██║╚██╗██║██║  ██║    ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
       ╚██████╔╝██████╔╝██████╔╝    ██║  ██║██║ ╚████║██████╔╝    ███████╗ ╚████╔╝ ███████╗██║ ╚████║
        ╚═════╝ ╚═════╝ ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝     ╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ 
        
        ============================================================================================     
""")
# =======================================================================================================

# =========================== DEVELOPMENT AND DISPLAY ===================================================
number = int(input("Which number do you want to check? "))

remainder = number % 2

if remainder == 0:
    print(f"{number} is an even number! because it remainder is = {remainder}")
else:
    print(f"{number} is an odd number! because it remainder is = {remainder}")
# =======================================================================================================