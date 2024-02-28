import unittest
from datetime import datetime
from calculadora import CalculadoraLiquidacion 

class TestCalculadoraLiquidacion(unittest.TestCase):
    def setUp(self):
        self.calculadora = CalculadoraLiquidacion()

    def test_caso_prueba_real(self):
        motivo= "Renuncia"
        salario_basico = 2000000
        fecha_inicio_labores = "01/01/2023"
        fecha_ultimas_vacaciones = "01/07/2023"
        dias_acumulados_vacaciones = 5

        indemnizacion = self.calculadora.calcular_liquidacion(salario_basico, fecha_inicio_labores, fecha_ultimas_vacaciones)
        vacaciones = self.calculadora.calcular_vacaciones(salario_basico, dias_acumulados_vacaciones)
        cesantias = self.calculadora.calcular_cesantias(salario_basico, dias_acumulados_vacaciones)
        intereses_cesantias = self.calculadora.calcular_intereses_cesantias(cesantias, vacaciones)
        primas = self.calculadora.calcular_prima(salario_basico, dias_acumulados_vacaciones)
        retencion_fuente = self.calculadora.calcular_retencion(indemnizacion + vacaciones + cesantias + intereses_cesantias + primas)
        total_pagar = indemnizacion + vacaciones + cesantias + intereses_cesantias + primas - retencion_fuente

        self.assertAlmostEqual(indemnizacion, 0, delta=0.01)
        self.assertAlmostEqual(vacaciones, 544257, delta=0.01)
        self.assertAlmostEqual(cesantias, 1088514, delta=0.01)
        self.assertAlmostEqual(intereses_cesantias, 65674, delta=0.01)
        self.assertAlmostEqual(primas, 1082500, delta=0.01)
        self.assertAlmostEqual(retencion_fuente, 28154.64, delta=0.01)
        self.assertAlmostEqual(total_pagar, 2809099, delta=0.01)

    def test_calculate_liquidacion(self):
        salario = 2000000
        fecha_inicio = "01/01/2022"
        fecha_fin = "01/01/2023"
        result = self.calculadora.calcular_liquidacion(salario, fecha_inicio, fecha_fin)
        self.assertEqual(result, 2165000 )  

    def test_calculate_indemnizacion(self):
        salario = 2000000
        motivo = "despido"
        fecha_inicio = "01/01/2022"
        fecha_fin = "15/01/2022"
        meses_trabajados = 6
        result = self.calculadora.calcular_indemnizacion(salario, motivo, meses_trabajados,  fecha_inicio, fecha_fin)
        self.assertEqual(result, 6000000) 

    def test_calculate_vacaciones(self):
        salario = 2000000
        fecha_inicio = "01/01/2022"
        fecha_fin = "15/01/2022"
        dias_trabajados = 10
        result = self.calculadora.calcular_vacaciones(salario, dias_trabajados,  fecha_inicio, fecha_fin)
        self.assertEqual(result, 66666)  

    def test_calculate_cesantias(self):
        salario_mensual = 2000000
        fecha_inicio = "01/01/2022"
        fecha_fin = "15/01/2022"
        dias_trabajados = 15
        result = self.calculadora.calcular_cesantias(salario_mensual, dias_trabajados,  fecha_inicio, fecha_fin)
        self.assertEqual(result, 50000)  

    def test_calculate_prima(self):
        salario_mensual = 2000000
        fecha_inicio = "01/01/2022"
        fecha_fin = "15/01/2022"
        dias_trabajados = 20
        result = self.calculadora.calcular_prima(salario_mensual, dias_trabajados,  fecha_inicio, fecha_fin)
        self.assertEqual(result, 55556) 

    def test_calculate_retencion(self):
        salario = 5000000
        fecha_inicio = "01/01/2022"
        fecha_fin = "15/01/2022"
        result = self.calculadora.calcular_retencion(salario,  fecha_inicio, fecha_fin)
        self.assertEqual(result, 0) 

    def test_invalid_date_format_calculate_liquidacion(self):
        salario = 2000000
        fecha_inicio = "01-01-2022"  
        fecha_fin = "15-01-2022"    
        with self.assertRaises(ValueError):
            self.calculadora.calcular_liquidacion(salario, fecha_inicio, fecha_fin)

    def test_invalid_motivo_calculate_indemnizacion(self):
        salario = 2000000
        motivo = "Renuncia" 
        meses_trabajados = 6
        with self.assertRaises(ValueError):
            self.calculadora.calcular_indemnizacion(salario, motivo, meses_trabajados)

    def test_negative_dias_trabajados_calculate_vacaciones(self):
        salario_mensual = 2000000
        dias_trabajados = -5 
        with self.assertRaises(ValueError):
            self.calculadora.calcular_vacaciones(salario_mensual, dias_trabajados)

    def test_negative_dias_trabajados_calculate_cesantias(self):
        salario_mensual = 2000000
        dias_trabajados = -10  
        with self.assertRaises(ValueError):
            self.calculadora.calcular_cesantias(salario_mensual, dias_trabajados)

    def test_invalid_ingreso_laboral_calculate_retencion(self):
        ingreso_laboral = "5000000"  
        with self.assertRaises(ValueError):
            self.calculadora.calcular_retencion(ingreso_laboral)

    def test_negative_total_pagar_print_results(self):
        indemnizacion = 500000
        vacaciones = 100000
        cesantias = 80000
        intereses_cesantias = 12000
        primas = 15000
        retencion_fuente = 5000
        total_pagar = -(indemnizacion + vacaciones + cesantias + intereses_cesantias + primas + retencion_fuente)
        with self.assertRaises(ValueError):
            pass  

    def test_invalid_fecha_inicio_format(self):
        with self.assertRaises(ValueError):
            self.calculadora.calcular_liquidacion(2000000, "01-01-2022", "01/01/2023")

    def test_invalid_fecha_ultimas_vacaciones_format(self):
        with self.assertRaises(ValueError):
            self.calculadora.calcular_liquidacion(2000000, "01/01/2022", "2023/01/01")

    def test_invalid_motivo_terminacion(self):
        with self.assertRaises(ValueError):
            self.calculadora.calcular_indemnizacion(2000000, "Despido Masivo", 12)

    def test_negative_salario_basico(self):
        with self.assertRaises(ValueError):
            self.calculadora.calcular_liquidacion(-2000000, "01/01/2022", "01/01/2023")

    def test_negative_dias_acumulados_vacaciones(self):
        with self.assertRaises(ValueError):
            self.calculadora.calcular_vacaciones(2000000, -10)

    def test_invalid_ingreso_laboral_type(self):
        with self.assertRaises(ValueError):
            self.calculadora.calcular_retencion("five million")

if __name__ == '__main__':
    unittest.main()
