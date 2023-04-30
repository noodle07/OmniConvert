import os

# Limpa a tela do console
def clear_screen(msg=""):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(msg)

clear_screen()

while True:
    def decimal_to_binary(decimal):
        return bin(decimal)[2:]

    def binary_to_decimal(binary):
        return int(binary, 2)

    def hexadecimal_to_decimal(hexadecimal):
        return int(hexadecimal, 16)

    def decimal_to_hexadecimal(decimal):
        return hex(decimal)[2:]

    def binary_to_hexadecimal(binary):
        decimal = binary_to_decimal(binary)
        return decimal_to_hexadecimal(decimal)

    def hexadecimal_to_binary(hexadecimal):
        decimal = hexadecimal_to_decimal(hexadecimal)
        return decimal_to_binary(decimal)
    
    def ascii_to_binary(caracter):
        return bin(ord(caracter))[2:]
    
    def ascii_to_decimal(caracter):
        return ord(caracter)
    
    def ascii_to_hexadecimal(caracter):
        return hex(ord(caracter))[2:]
    
    def decimal_to_ascii(decimal):
        return chr(decimal)
    
    def binary_to_ascii(binary):
        return chr(int(binario, 2))
    
    def hexadecimal_to_ascii(hexadecimal):
        return chr(int(hexadecimal, 16))
    
    # exibe menu de opções
    print("Selecione uma opção:")
    print("1 - Decimal para binário")
    print("2 - Binário para decimal")
    print("3 - Hexadecimal para decimal")
    print("4 - Decimal para hexadecimal")
    print("5 - Binário para hexadecimal")
    print("6 - Hexadecimal para binário")
    print("7 - ASCII para binario")
    print("8 - ASCII para decimal")
    print("9 - ASCII para hexadecimal")
    print("10 - Decimal para ASCII")
    print("11 - Binario para ASCII")
    print("12 - Hexadecimal para ASCII")
    print("0 - Sair do programa")

    opcao = int(input("Digite sua opção (1/2/3/4/5/6/7/8/9/10/11/12/0): "))
    
    #DECIMAL TO BINARY
    if opcao == 1:
        decimal = int(input("Digite um número decimal: "))
        resultado = decimal_to_binary(decimal)
        clear_screen(f"O número {decimal} em binário é {resultado}")

    #BINARY TO DECIMAL
    elif opcao == 2:
        binary = input("Digite um número binário: ")
        resultado = binary_to_decimal(binary)
        clear_screen(f"O número binário {binary} em decimal é {resultado}")
    
    #HEXADECIMAL TO DECIMAL
    elif opcao == 3:
        hexadecimal = input("Digite um número hexadecimal: ")
        resultado = hexadecimal_to_decimal(hexadecimal)
        clear_screen(f"O número hexadecimal {hexadecimal} em decimal é {resultado}")

    #DECIMAL TO HEXADECIMAL
    elif opcao == 4:
        decimal = int(input("Digite um número decimal: "))
        resultado = decimal_to_hexadecimal(decimal)
        clear_screen(f"O número decimal {decimal} em hexadecimal é {resultado}")

    #BINARY TO HEXADECIMAL
    elif opcao == 5:
        binary = input("Digite um número binário: ")
        resultado = binary_to_hexadecimal(binary)
        clear_screen(f"O número binário {binary} em hexadecimal é {resultado}")

    #HEXADECIMAL TO BINARY
    elif opcao == 6:
        hexadecimal = input("Digite um número hexadecimal: ")
        resultado = hexadecimal_to_binary(hexadecimal)
        clear_screen(f"O número hexadecimal {hexadecimal} em binário é {resultado}")

    #ASCII TO BINARY
    elif opcao == 7:
        #solicita o input do usario
        caracter = input("Digite um caracter: ")
        resultado = ascii_to_binary(caracter)
        clear_screen(f"O caracter ASCII {caracter} em binario é {resultado}")

    #ASCII TO DECIMAL
    elif opcao == 8:
        caracter = input("Digite um caracter: ")
        resultado = ascii_to_decimal(caracter)
        clear_screen(f"O caracter {caracter} em decimal é {resultado}")

    #ASCII TO HEXADECIMAL
    elif opcao == 9:
        caracter = input("Digite um caracter: ")
        resultado = ascii_to_hexadecimal(caracter)
        clear_screen(f"O caracter {caracter} em hexadecimal é {resultado}")

    #DECIMAL TO ASCII
    elif opcao == 10:
        decimal = int(input("Digite um numero decimal: "))
        resultado = decimal_to_ascii(decimal)
        clear_screen(f"O numero decimal {decimal} em ASCII é {resultado}")

    #BINARY TO ASCII
    elif opcao == 11:#bin
        binario = input("Digite um numero binario: ")
        resultado = binary_to_ascii(binario)
        clear_screen(f"O numero binario {binario} em ASCII é {resultado}")

    #HEXADECIMAL TO ASCII
    elif opcao == 12:#hex
        hexadecimal = input("Digite um numero hexadecimal: ")
        resultado = hexadecimal_to_ascii(hexadecimal)
        clear_screen(f"O numero hexadecimal {hexadecimal} em ASCII é {resultado}")

    #END PROGRAM
    elif opcao == 0:
        clear_screen()
        clear_screen("O programa foi encerrado")
        break
    else: #IF INVALID OPTION
        clear_screen("Opção inválida. Por favor, escolha uma opção válida (1/2/3/4/5/6/7/8/9/10/11/12).")
