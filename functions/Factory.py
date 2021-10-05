from functions.Calculator import Calculator


class CalculateFactory():
    def __init__(self, expression) -> None:
        self._expression = expression
        self._cal = Calculator()

    def calculate(self) -> float:
        result = self._expression[0]

        for index in range(1, len(self._expression), 2):
            if self._expression[index] == "-":
                result = self._cal.subtraction(result, self._expression[index+1])
            elif self._expression[index] == "+":
                result = self._cal.addition(result, self._expression[index+1])
            elif self._expression[index] == "/":
                result = self._cal.division(result, self._expression[index+1])
            elif self._expression[index] == "*":
                result = self._cal.multiplication(result, self._expression[index+1])
         
        return result
