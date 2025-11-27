from django.db import models

class Student(models.Model):
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    average = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.forename} {self.surname} {self.major}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    score = models.FloatField()
    
    def __str__(self):
        return f"{self.student.forename} {self.student.surname} - {self.course}: {self.score}" 