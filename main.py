class Calculator:
    def add(self,a:float, b:float)-> float:
        return a+b

    def sub(self,a:float, b:float)-> float:
        return a-b

    def mul(self,a:float, b:float)-> float:
        return a*b

    def div(self,a:float, b:float)-> float:
        if b==0:
            raise ValueError("Cannot divide by zero")
        return a/b