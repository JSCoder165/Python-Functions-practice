import math
from sys import set_coroutine_origin_tracking_depth
from unicodedata import name


class Student(object):
  
  def __init__(self, name, age, gender, GPA, grades = None):
    self.name = name
    self.age = age
    self.gender = gender
    self.GPA = GPA
    self.grades = grades or {}

  def set_grade(self, subject, grade):
    self.grades[subject] = grade

  def get_grade(self, subject):
    return self.grades[subject]
  
  def get_GPA(self):
    return sum(self.grades.values())/len(self.grades)

John = Student("John", 15, "Male", 4, {"math": "5"})

print(John.set_grade())