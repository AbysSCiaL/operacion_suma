import unittest
from operaciones_aritmeticas import OperacionesAritmeticas

class TestSuma(unittest.TestCase):
    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange
        operando1 = 10
        operando2 = 15
        resultadoEsperado = 25

        objOperaciones = OperacionesAritmeticas(operando1, operando2)
        # Act
        resultadoActual = objOperaciones.calcularSuma()
        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual, "Fallo la suma")

    def test_suma_operadorNoNumerico_lanzaExcepcion(self):
        objOperaciones = OperacionesAritmeticas(3, "a")
        with self.assertRaises(TypeError):
            objOperaciones.calcularSuma()

class TestDivision(unittest.TestCase):
    def test_division_dosNumeros_retornaDivision(self):
        # Arrange
        dividendo = 10
        divisor = 15
        resultadoEsperado = 0.667

        objOperaciones = OperacionesAritmeticas(dividendo, divisor)
        # Act
        resultadoActual = objOperaciones.calcular_division()
        # Assert
        self.assertAlmostEqual(resultadoEsperado, resultadoActual, 3, "Fallo la division")

    def test_division_operadorNoNumerico_lanzaExcepcion(self):
        objOperaciones = OperacionesAritmeticas(3, "a")
        with self.assertRaises(TypeError):
            objOperaciones.calcular_division()

if __name__ == '__main__':
    unittest.main()
