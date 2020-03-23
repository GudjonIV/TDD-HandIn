# Author: Guðjón Ingi Valdimarsson
# Date: 23.03.2020

class Calculator():
    @staticmethod
    def add(input_string: str) -> int:
        if input_string == "":
            return 0
        input_list = input_string.replace("\n", ",").split(",")
        input_list = [int(value) for value in input_list if int(value) <= 1000]
        negatives_string = ",".join([str(value) for value in input_list if value < 0])
        if negatives_string:
            raise ValueError("Negatives not allowed: {}".format(negatives_string))
        elif len(input_list) >= 2:
            ret_value = 0
            for value in input_list:
                ret_value += int(value)
            return ret_value
        else:
            return input_list[0]