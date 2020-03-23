# Author: Guðjón Ingi Valdimarsson
# Date: 23.03.2020

from calculator import Calculator

def testEmptyAdd() -> None:
    assert Calculator.add("") == 0