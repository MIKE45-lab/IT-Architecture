from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    score = models.FloatField()
    
    def __str__(self):
        return f"{self.student.name} - {self.course}: {self.score}" 