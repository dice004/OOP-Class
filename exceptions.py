# Before Exceptions
class Division:

    def divide_me(self,num, denom):
        return num/denom
    
division = Division()
print(division.divide_me(4,2))

#After Exceptions
class Converter:

    def divide(self, num,denom):
        try:
            result = num / denom
        except ZeroDivisionError:
            print("Can't do this ")

converter = Converter()
converter.divide(6,2)
# Two Exceptions
class Converter:

    def divide(self, num,denom):
        try:
            result = num / denom
        except (ZeroDivisionError, TypeError) as e:
            print(f"Can't do this - {e} ")



# Another way to capture more errors
class Converter:

    def divide(self, num,denom):
        try:
            result = num / denom
        except ZeroDivisionError:
            print("Can't do this ")
        except SyntaxError:
            print("Syntax error")