from product.calculator.Caculator import Calculator


class BasicCalculator(Calculator):
    def calculate(self) -> float:
        result = self._expression[0]

        for index in range(1, len(self._expression), 2):
            if self._expression[index] == "-":
                result = self.subtraction(result, self._expression[index+1])
            elif self._expression[index] == "+":
                result = self.addition(result, self._expression[index+1])
            elif self._expression[index] == "/":
                result = self.division(result, self._expression[index+1])
            elif self._expression[index] == "*":
                result = self.multiplication(result, self._expression[index+1])
        
        return result

    def subtraction(self, num_one, num_twoo) -> float:
        return num_one - num_twoo

    def addition(self, num_one, num_twoo) -> float:
        return num_one + num_twoo

    def multiplication(self, num_one, num_twoo) -> float:
        return num_one * num_twoo

    def division(self, num_one, num_twoo) -> float:
        return num_one / num_twoo
