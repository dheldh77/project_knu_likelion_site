from django.shortcuts import render, get_object_or_404, redirect
from .models import QNA
from django.utils import timezone
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger 

# Create your views here.
def qna(request):
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
        
    qnas = QNA.objects.all().order_by('-id')

    p = Paginator(qnas, 10)

    people = p.page(page)
    return render(request,'qna.html', {'qnas':people})

def create(request):
    qna = QNA()
    qna.title = request.GET['title']
    qna.body = request.GET['body']
    qna.pub_date = timezone.datetime.now()
    qna.save()
    return redirect('/qna/'+str(qna.id))

def new(request):
    return render(request,'qna_new.html')

def detail(request, qna_num):
    qna = get_object_or_404(QNA,pk=qna_num)

    #맨 처음 글
    if(QNA.objects.first() == qna):
        prev = 0
    else:
        prev = qna.id - 1

    #맨 마지막 글
    if(QNA.objects.last() == qna):
        next = 0
    else:
        next = qna.id + 1

    return render(request,'qna_detail.html',{'qna':qna, 'prev':prev, 'next':next})