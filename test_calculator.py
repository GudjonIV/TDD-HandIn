# Author: Guðjón Ingi Valdimarsson
# Date: 23.03.2020

from calculator import Calculator

def testEmptyAdd() -> None:
    assert Calculator.add("") == 0

def testOneNumberAdd() -> None:
    assert Calculator.add("1") == 1

def testTwoNumbersAdd() -> None:
    assert Calculator.add("5,3") == 8

def testManyNumbersAdd() -> None:
    assert Calculator.add("10,20,9,17,15") == 71

def testNewLineAdd() -> None:
    assert Calculator.add("15\n7") == 22

def testBiggerThan1000Add() -> None:
    assert Calculator.add("1001,14") == 14