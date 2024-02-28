from datetime import datetime

class CalculadoraLiquidacion:
    def __init__(self, valor_uvt=39205):
        self.valor_uvt = valor_uvt

    def calcular_liquidacion(self, salario, fecha_inicio, fecha_fin):
        fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y") 
        fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")
        dias_totales = (fecha_fin - fecha_inicio).days + 1  
        dias_faltantes = 30 - fecha_fin.day

        # Calcular liquidación 
        valor_diario = salario / 30
        liquidacion = valor_diario * dias_faltantes

        return round(liquidacion)

    def calcular_indemnizacion(self, salario, motivo, meses_trabajados):
        # Calcular indemnización según motivo de finalización
        factor_despido = 0.5 if motivo.lower() == 'despido' else 0.0
        valor_indemnizacion = salario * meses_trabajados * factor_despido

        return valor_indemnizacion

    def calcular_vacaciones(self, salario_mensual, dias_trabajados):
        valor_diario = salario_mensual / 30  
        valor_vacaciones = (salario_mensual * dias_trabajados) / 720

        return round(valor_vacaciones)

    def calcular_cesantias(self, salario_mensual, dias_trabajados):
        cesantias = (salario_mensual * dias_trabajados) / 360  
        return round(cesantias)

    def calcular_intereses_cesantias(self, cesantias, vacaciones):
        # Calcular valor de intereses de cesantías
        valor_intereses_cesantias = (cesantias + vacaciones) * 0.12
        return valor_intereses_cesantias

    def calcular_prima(self, salario_mensual, dias_trabajados):
        prima = salario_mensual * (dias_trabajados / 360) 
        return round(prima / 2)

    def calcular_retencion(self, ingreso_laboral):
        retencion = 0  # Initialize with a default value

        if ingreso_laboral <= 42412:
            pass  # 
        elif ingreso_laboral <= 636132:
            ingreso_uvt = ingreso_laboral / self.valor_uvt
            base_uvt = ingreso_uvt - 95
            base_pesos = base_uvt * self.valor_uvt  
            retencion = (base_pesos * 0.19) + (10 * self.valor_uvt)

        return round(retencion)
# Entradas del usuario
motivo_terminacion = input("Motivo de finalización de contrato (renuncia o despido): ")
salario_basico = float(input("Salario básico del empleado: "))
fecha_inicio_labores = input("Fecha de inicio de labores (DD/MM/YYYY): ")
fecha_ultimas_vacaciones = input("Fecha de últimas vacaciones (DD/MM/YYYY): ")
dias_acumulados_vacaciones = int(input("Días de vacaciones acumulados: "))

calculadora = CalculadoraLiquidacion()

indemnizacion = calculadora.calcular_liquidacion(salario_basico, fecha_inicio_labores, fecha_ultimas_vacaciones)
vacaciones = calculadora.calcular_vacaciones(salario_basico, dias_acumulados_vacaciones)
cesantias = calculadora.calcular_cesantias(salario_basico, dias_acumulados_vacaciones)
intereses_cesantias = calculadora.calcular_intereses_cesantias(cesantias, vacaciones)
primas = calculadora.calcular_prima(salario_basico, dias_acumulados_vacaciones)  
total_pagar = indemnizacion + vacaciones + cesantias + intereses_cesantias + primas
retencion_fuente = calculadora.calcular_retencion(total_pagar)

print("\n--- Resultados ---")
print(f"Indemnización: ${indemnizacion:,.2f}")
print(f"Vacaciones: ${vacaciones:,.2f}")
print(f"Cesantías: ${cesantias:,.2f}")
print(f"Intereses de cesantías: ${intereses_cesantias:,.2f}")
print(f"Primas: ${primas:,.2f}")
print(f"Retención en la fuente: ${retencion_fuente:,.2f}")
print(f"Total a pagar: ${total_pagar - retencion_fuente:,.2f}")
