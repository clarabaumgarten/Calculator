from factory.BasicCalculatorFactory import BasicCalculatorFactory
from factory.AdvancedCalculatorFactory import AdvancedCalculatorFactory


def turns_string_number_to_float(string_number):
    if string_number not in ('-', '+', '*', '/', '**', '//'):
        return float(string_number)
    return string_number


if __name__ == "__main__":
    expression = input("Digite uma expressão básica: ")
    expression = expression.split()
    expression = list(map(turns_string_number_to_float, expression))
    
    basic_cal = BasicCalculatorFactory(expression)
    basic_cal.calculate()
    basic_cal.show_result()

    expression = input("\n\nDigite uma expressão avançada: ")
    expression = expression.split()
    expression = list(map(turns_string_number_to_float, expression))

    advanced_cal = AdvancedCalculatorFactory(expression)
    advanced_cal.calculate()
    advanced_cal.show_result()