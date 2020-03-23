# Author: Guðjón Ingi Valdimarsson
# Date: 23.03.2020

class Calculator():
    @staticmethod
    def add(input_string: str) -> int:
        input_list = input_string.split(",")
        if input_string == "":
            return 0
        elif len(input_list) == 2:
            return int(input_list[0]) + int(input_list[1])
        else:
            return int(input_string)