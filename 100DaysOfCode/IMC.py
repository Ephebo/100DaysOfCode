# ========================= START =================================
print("""
 ___  _____ ______   ________     
|\  \|\   _ \  _   \|\   ____\    
\ \  \ \  \\\__\ \  \ \  \___|    
 \ \  \ \  \\|__| \  \ \  \       
  \ \  \ \  \    \ \  \ \  \____  
   \ \__\ \__\    \ \__\ \______\\
    \|__|\|__|     \|__|\|_______|
    
=================================================================
""")
# ======================= DEVELOPMENT =============================
peso = input("Digite seu peso em kg: ")
altura = input("digite sua altura em m: ")

imc = int(peso) / float(altura)**2
# Explicação
# IMC = peso/altura²
# ===============================================================

# ======================== DISPLAY ================================
print(f"""
=========================IMC=====================================
        Seu Índice de Massa Corporal é de {imc:.2f}
=================================================================
    """)
# ===============================================================
