# Calculadora

def calculadora_vagabunda():
    print("--- Calculadora Vagabunda ---")
    
    num_input = input("Digite o primeiro número: ")
    

    memoria = float(num_input)

    while True:
        op = input(f"Operação (+, -, *, /) sobre o valor {memoria} ou 's' para sair: ").lower()
        
        if op == 's': 
            break
        
        if op not in ['+', '-', '*', '/']:
            print("Operação inválida!")
            continue

        proximo_input = input("Digite o próximo número: ")
        
        if (proximo_input):
            proximo_num = float(proximo_input)
            
            if op == '+': memoria += proximo_num
            elif op == '-': memoria -= proximo_num
            elif op == '*': memoria *= proximo_num
            elif op == '/':
                if proximo_num == 0:
                    print("Erro: Divisão por zero!")
                else:
                    memoria /= proximo_num
            
            print(f"Resultado: {memoria}")
        else:
            print("Erro: Isso não é um número.")

calculadora_vagabunda()
