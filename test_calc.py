import pytest
from app.calculator import Calculator



class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_adding_success(self):
        assert self.calc.adding(self,9,7) == 16

    def test_division(self):
        assert self.calc.division(self,27,9) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,2,0)

    def test_multiply(self):
        assert self.calc.multiply(self,5,4) == 20

    def test_subtraction(self):
        assert self.calc.subtraction(self,9,6) == 3

    def teardown(self):
        print('Выполнение Teardown')