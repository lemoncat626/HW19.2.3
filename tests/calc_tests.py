import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calc_correctly(self):
        assert self.calc.multiply(self, 4, 7) == 28

    def test_division_calc_correctly(self):
        assert self.calc.division(self, 9, 3) == 3

    def test_subtraction_calc_correctly(self):
        assert self.calc.subtraction(self, 8, 5) == 3

    def test_adding_calc_correctly(self):
        assert self.calc.adding(self, 6, 7) == 13
