#===============================================================================================
# Projeto Calculadora Simples
#===============================================================================================

def calculadora():
    print("===== CALCULADORA =====")
    print("Escolha uma operação: ")
    print("1 - Soma ")
    print("2 - Subtração ")
    print("3 - Multiplicação ")
    print("4 - Divisão ")
    print("========================")
    
    opcao = input("Digite o número da operação: ")
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if opcao == "1":
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    
    elif opcao == "2":
          resultado = num1 - num2
          print(f"Resultado: {num1} - {num2} = {resultado}")
    
    elif opcao == "3":
              resultado = num1 * num2
              print(f"Resultado: {num1} x {num2} = {resultado}")   

    elif opcao == "4":
        if num2 == 0:
              print("Erro: Não é possível dividir por zero!") 
        else:           
              resultado = num1 / num2
              print(f"Resultado: {num1} / {num2} = {resultado:.2f}") 
    else:
          print("Opção inválida! Escolha entre 1 e 4.")

calculadora()
        

