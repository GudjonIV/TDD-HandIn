# Author: Guðjón Ingi Valdimarsson
# Date: 23.03.2020

class Calculator():
    @staticmethod
    def add(input_string: str) -> int:
        input_list = input_string.replace("\n", ",").split(",")
        if input_string == "":
            return 0
        elif len(input_list) >= 2:
            ret_value = 0
            for value in input_list:
                ret_value += int(value)
            return ret_value
        else:
            return int(input_string)