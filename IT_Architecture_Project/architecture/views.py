from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student, Grade
from django.db.models import Avg

@login_required
def dashboard(request):
   avg_scores = Grade.objects.values('course').annotate(avg_score=Avg('score'))
   student_count = Student.objects.count() 
   return render(request, 'architecture/dashboard.html', {
       'avg_scores': list(avg_scores),
       'student_count': student_count
   })
   
   def students(request):
       students = Student.objects.all()
       return render(request, 'architecture/students.html', {'students': students})