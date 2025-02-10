class Calculator:
    """ 计算器 """
    def __init__(self):
        """ 数据初始化 """
        self.result = 0

    def calculate(self):
        self.result = float(input())

        while True:
            operator = input()
            if operator == "=":
                break

            temp_var_b = float(input())

            if operator == "+":
                self.result = self.result + temp_var_b
            if operator == "-":
                self.result = self.result - temp_var_b
            if operator == "*":
                self.result = self.result * temp_var_b
            if operator == "/":
                self.result = self.result / temp_var_b

        print(f"RESULT IS {self.result}")


if __name__ == '__main__':
    c = Calculator()
    c.calculate()
