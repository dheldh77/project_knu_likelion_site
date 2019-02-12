from django.shortcuts import render
from .models import Student
from .models import Teacher
import random

# Create your views here.
def shuffle(request):
        #뒤섞는 함수!
        def chunks(l,n):
                for i in range(0, len(l), n):
                        yield l[i:i+n]

        #학생 뒤썩어 줘라 자슥
        s_names = list(Student.objects.all().order_by('-id'))
        random.shuffle(s_names)
        s_suf = list(chunks(s_names,3))

        t_names = list(Teacher.objects.all().order_by('-id'))

        total ={ k : v for k,v in zip(t_names, s_suf) }

        return render(request,'shuffle.html', { 'total':total, })