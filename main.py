class Calculator:
    """ 计算器 """
    def __init__(self):
        """ 数据初始化 """
        self.result = 0

    def calculate(self):
        self.result = float(input())
        operators = ['+', '-', '*', '/', '=']

        while True:
            operator = input()  # 运算符

            # 判断运算符是否合规
            if operator not in operators:
                print("Invalid input!")
                break
            else:
                # 是否退出程序的关键语句！
                if operator == "=":
                    break

                # 临时变量
                temp_var_b = float(input())

                if operator == "+":
                    self.result = self.result + temp_var_b
                elif operator == "-":
                    self.result = self.result - temp_var_b
                elif operator == "*":
                    self.result = self.result * temp_var_b
                elif operator == "/":
                    self.result = self.result / temp_var_b

        print(f"RESULT IS {self.result}")


if __name__ == '__main__':
    c = Calculator()
    c.calculate()
