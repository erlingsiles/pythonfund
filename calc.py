class Calculadora:
    def __init__(self):
        pass

    def sumar(self, num1, num2):
        resultado = num1+num2
        return resultado

    def restar(self, num1, num2):
        return num1 - num2

    def mult(self, num1, num2):
        return num1 * num2

    def divi(self, num1, num2):
        return num1 / num2

    def guardar(self, resultado):
        try:
            with open("Encuentro 4/datos_calc.txt","a") as file:
                file.write(f"{resultado}\n")
        except Exception as e:
            print("No se pudo guardar el resultado")


def main():
    mi_calculadora = Calculadora()

    while True:
        print("Mi Calculadora")
        print("1:Suma: ")
        print("2:restar: ")
        print("3:Multiplicar: ")
        print("4:Dividir: ")
        print("5:Salir")

        opcion = input("Elija una opcion")
    
        if opcion == "5":
            print("Esta saliendo de mi calculadora")
            break
        if opcion in ["1","2","3","4"]:
            try:
                num1 = float(input("Ingrese el primer valor"))
                num2 = float(input("ingrese el segundo valor"))
            except ValueError:
                print("Esta ingresando un valor no valido")
                continue

            if opcion == "1":
                resultado = mi_calculadora.sumar(num1, num2)
                print(resultado)    
    
            elif opcion == "2":

                resultado = mi_calculadora.restar(num1, num2)
                print(resultado)
            elif opcion=="3":
                resultado = mi_calculadora.mult(num1, num2)
                print(resultado)
            elif opcion=="4":
                resultado = mi_calculadora.divi(num1, num2)
                print(resultado)
            
            mi_calculadora.guardar(f"Operacion:{opcion},Números: ({num1},{num2},Resultado: {resultado})")            

main()