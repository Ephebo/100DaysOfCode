
# ========================== START ===============================================================

print("""
                            ████████╗██╗██████╗                                    
                            ╚══██╔══╝██║██╔══██╗                                   
                               ██║   ██║██████╔╝                                   
                               ██║   ██║██╔═══╝                                    
                               ██║   ██║██║                                        
                               ╚═╝   ╚═╝╚═╝                                        
                                                                                   
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
===================================================================================================================================================
      """)
# ========================== INPUT ==================================================================
bill = float(input("quanto custou a conta? "))
tip = int(input("quanto gorjeta você gostaria de atribuir? 10, 12, or 15? "))
split = int(input("Dividir para quantas pessoas? "))
# =================================================================================================

# ========================== DEVELOPMENT ============================================================
division = (bill/split)
convert = (tip * division) / 100
result = division + convert
# Explicação:

# division = (150/5)
# = 30
# convert = (12 * 30) / 100
# = 3.6
# result = 30 + 3.6 = 33.60
# =================================================================================================

# =========================== DISPLAY ===============================================================
print(f"Cada pessoa deve pagar: R${result:.2f}")
# =================================================================================================
