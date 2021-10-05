from functions.Factory import CalculateFactory


def turns_string_number_to_float(string_number):
    if string_number not in ('-', '+', '*', '/'):
        return float(string_number)
    return string_number

if __name__ == "__main__":
    expression = input("Digite uma expressão: ")
    expression = expression.split()
    expression = list(map(turns_string_number_to_float, expression))
    
    cal = CalculateFactory(expression)
    print(cal.calculate())
