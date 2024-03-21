from datetime import datetime

class InterfazCalculadora:
    def __init__(self):
        self.calculadora = CalculadoraLiquidacion()

    def obtener_datos(self):
        salario_basico = float(input("Ingrese el salario básico: "))
        fecha_inicio_labores = input("Ingrese la fecha de inicio de labores (formato dd/mm/yyyy): ")
        fecha_ultimas_vacaciones = input("Ingrese la fecha de las últimas vacaciones (formato dd/mm/yyyy): ")
        dias_acumulados_vacaciones = int(input("Ingrese los días acumulados de vacaciones: "))
        return salario_basico, fecha_inicio_labores, fecha_ultimas_vacaciones, dias_acumulados_vacaciones

    def mostrar_resultados(self):
        salario_basico, fecha_inicio_labores, fecha_ultimas_vacaciones, dias_acumulados_vacaciones = self.obtener_datos()
        resultados = self.calculadora.calcular_resultados_prueba(salario_basico, fecha_inicio_labores, fecha_ultimas_vacaciones, dias_acumulados_vacaciones)
        
        print("\nResultados de la liquidación:")
        print("Indemnización:", resultados[0])
        print("Vacaciones:", resultados[1])
        print("Cesantías:", resultados[2])
        print("Intereses de cesantías:", resultados[3])
        print("Prima:", resultados[4])
        print("Retención en la fuente:", resultados[5])
        print("Total a pagar:", resultados[6])

if __name__ == "__main__":
    interfaz = InterfazCalculadora()
    interfaz.mostrar_resultados()
