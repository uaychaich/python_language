class Person:
    numberofeye=2
    def __init__(self,name,salary=0):
        self.name = name
        self.salary=salary
    
    def tax(self,taxrate):
        return self.salary*taxrate
    
    def __str__(self):
        return f"{self.name} {self.salary} naja"
    
    def __eq__(self, value):
        return self.salary== value
    
def HelloWorld():
    return 'Hello World!!'

UayVar = 'Uaychai'