class Calculadora:
    def __init__(self):
        pass  # No se necesitan atributos iniciales

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"

def main():
    while True:
        calc = Calculadora()
        print("Calculadora Básica")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")

        opcion = input("Elige una opción (1/2/3/4): ")
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Primer número: "))
                num2 = float(input("Segundo número: "))
            except ValueError:
                print("Entrada inválida.")
                continue

            if opcion == '1':
                resultado = calc.sumar(num1, num2)
            elif opcion == '2':
                resultado = calc.restar(num1, num2)
            elif opcion == '3':
                resultado = calc.multiplicar(num1, num2)
            elif opcion == '4':
                resultado = calc.dividir(num1, num2)

            print(f"Resultado: {resultado}")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
