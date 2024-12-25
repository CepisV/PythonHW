class Parent:
    def __init__(self, text=""):
        self.text = text

    def set_text(self, text=""):
        self.text = text

    def __str__(self):
        return f"Текстовое поле: {self.text}"


class Child(Parent):
    def __init__(self, text, number=0):
        super().__init__(text) 
        self.number = number

    def set_number(self, number):
        self.number = number

    def __str__(self):
        return f"Текстовое поле: {self.text}, Числовое поле: {self.number}"


parent_obj = Parent("Step Academy")
print(parent_obj)  

parent_obj.set_text("Новый текст")
print(parent_obj)  

child_obj = Child("Академия ШАГ", 42)
print(child_obj)  

child_obj.set_text("Обновленный текст")
child_obj.set_number(100)
print(child_obj)  
