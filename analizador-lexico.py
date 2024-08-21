#operatorsall = ['>', '<', '<=', '>=', '+', '-', '*', '/', '%', '**', '//', '=', '+=', '-=', '==', '*=', '/=', '%=', '//=', '!=', '&=', '|=', '^=', '>>=', '<<=']

operadores_logicos = ["+", "*", "/", "-"]
operadores_asignacion = ["="] 
numeros = [chr(i) for i in range(48, 58)]
letras = [chr(i) for i in range(97, 123)]
vartemp = ""
candenaf = input("ingresar cadena: ")
candena = ""

for i in candenaf:
    if i != "":
        candena = candena + i

for i in range(len(candena)):
    if candena[i].lower() in letras or candena[i] in numeros:
        vartemp = vartemp + candena[i]
        print(vartemp)
        if i != len(candena) - 1:
            if candena[i + 1] in operadores_logicos or candena[i + 1] in operadores_asignacion:
                print("Variable             :   " + vartemp)
                vartemp = ""
    elif candena[i] in operadores_logicos:
        print("Operador lógico      :   " + candena[i])
    elif candena[i] in operadores_asignacion:
        print("Operador asignación  :   " + candena[i])
