from datetime import datetime

class CalculadoraLiquidacion:
    def __init__(self, valor_uvt=39205):
        self.valor_uvt = valor_uvt

    def calcular_resultados_prueba(self, salario_basico, fecha_inicio_labores, fecha_ultimas_vacaciones, dias_acumulados_vacaciones):
        indemnizacion = self.calcular_liquidacion(salario_basico, fecha_inicio_labores, fecha_ultimas_vacaciones)
        vacaciones = self.calcular_vacaciones(salario_basico, dias_acumulados_vacaciones)
        cesantias = self.calcular_cesantias(salario_basico, dias_acumulados_vacaciones)
        intereses_cesantias = self.calcular_intereses_cesantias(cesantias, vacaciones)
        primas = self.calcular_prima(salario_basico, dias_acumulados_vacaciones)
        retencion_fuente = self.calcular_retencion(indemnizacion + vacaciones + cesantias + intereses_cesantias + primas)
        total_pagar = indemnizacion + vacaciones + cesantias + intereses_cesantias + primas - retencion_fuente
        return indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente, total_pagar

    def calcular_liquidacion(self, salario, fecha_inicio, fecha_fin):
        fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")
        dias_totales = (fecha_fin - fecha_inicio).days + 1
        dias_faltantes = 30 - fecha_fin.day
        valor_diario = salario / 30
        liquidacion = valor_diario * dias_faltantes

        return round(liquidacion)

    def calcular_indemnizacion(self, salario, motivo, meses_trabajados):
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
        valor_intereses_cesantias = (cesantias + vacaciones) * 0.12
        return valor_intereses_cesantias

    def calcular_prima(self, salario_mensual, dias_trabajados):
        prima = salario_mensual * (dias_trabajados / 360)
        return round(prima / 2)

    def calcular_retencion(self, salario_basico):
        retencion = 0

        salario_basico = float(salario_basico)

        if salario_basico <= 42412:
            pass
        elif salario_basico <= 636132:
            ingreso_uvt = salario_basico / self.valor_uvt
            base_uvt = ingreso_uvt - 95
            base_pesos = base_uvt * self.valor_uvt
            retencion = (base_pesos * 0.19) + (10 * self.valor_uvt)

        return round(retencion)
