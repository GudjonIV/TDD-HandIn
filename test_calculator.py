# Author: Guðjón Ingi Valdimarsson
# Date: 23.03.2020

from calculator import Calculator

def testEmptyAdd() -> None:
    assert Calculator.add("") == 0

def testOneNumberAdd() -> None:
    assert Calculator.add("1") == 1

def testTwoNumbersAdd() -> None:
    assert Calculator.add("5,3") == 8