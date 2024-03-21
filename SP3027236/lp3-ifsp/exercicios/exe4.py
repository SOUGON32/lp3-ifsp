def verificar_identificador_funcionario(identificador):


    if len(identificador) != 7:
        return False


    if not identificador.startswith("BR"):
        return False


    try:
        numero = int(identificador[2:6])
    except ValueError:
        return False


    if not identificador.endswith("X"):
        return False

    return True

identificador = input("Digite o identificador do funcionário: ")

if verificar_identificador_funcionario(identificador):
    print("Identificador válido")
else:
    print("Identificador inválido")
