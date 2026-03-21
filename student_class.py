class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def study(self):
        print(f'{self.name} is studying.')

    def get_info(self):
        return f'Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}'

# Example of creating and using student objects
if __name__ == '__main__':
    student1 = Student('Alice', 20, 'S001')
    student2 = Student('Bob', 22, 'S002')
    
    student1.study()
    print(student1.get_info())
    
    student2.study()
    print(student2.get_info())