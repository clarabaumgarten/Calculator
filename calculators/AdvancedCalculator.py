from calculators.Caculator import Calculator


class AdvancedCalculator(Calculator):
    def calculate(self) -> float:
        result = self._expression[0]

        for index in range(1, len(self._expression), 2):
            if self._expression[index] == "**":
                result = self.pow(result, self._expression[index+1])
            elif self._expression[index] == "//":
                result = self.sqrt(result, self._expression[index+1])
        
        return result

    def pow(self, num_one, num_twoo) -> float:
        return num_one ** num_twoo

    def sqrt(self, num_one, num_twoo) -> float:
        expo = 1 / num_twoo
        return num_one ** expo
