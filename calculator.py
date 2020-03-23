# Author: Guðjón Ingi Valdimarsson
# Date: 23.03.2020

class Calculator():
    def add(input_string: str) -> int:
        if input_string == "":
            return 0
        else:
            return int(input_string)