from django.shortcuts import render, get_object_or_404, redirect
from .models import QNA, Photo
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
    return render(request,'qna/qna.html', {'qnas':people})

def create(request):
    qna = QNA()
    qna.user = request.user
    qna.title = request.POST['title']
    qna.body = request.POST['body']
    qna.pub_date = timezone.now()
    qna.save()
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    for afile in request.FILES.getlist('file'):
        img = Photo()
        img.qna = qna
        img.image = afile
        img.save()
    
    return redirect('/qna/'+str(qna.id))

# def new(request):
#     return render(request,'qna/new.html')

def detail(request, qna_id):
    qna = get_object_or_404(QNA,pk=qna_id)

    #맨 처음 글
    if(QNA.objects.first() == qna):
        prev = 0
    else:
        prev = qna.id - 1

    #맨 마지막 글
    if(QNA.objects.last() == qna):
        next_ = 0
    else:
        next_ = qna.id + 1
    
    if (qna.user == request.user):
        canEdit = True
    else:
        canEdit = False
    
    return render(request,'qna/detail.html',{'qna':qna, 'prev':prev, 'next':next_, 'canEdit':canEdit})

def delete(request, qna_id):
    get_object_or_404(QNA, pk=qna_id).delete()

    return redirect('/qna/')

def edit(request, qna_id):
    post = get_object_or_404(QNA, pk=qna_id)
    return render(request, 'qna/edit.html', {'post':post})

def update(request, qna_id):
    qna = get_object_or_404(QNA, pk=qna_id)
    qna.title = request.GET['title']
    qna.body = request.GET['body']
    qna.save()
    return redirect('/qna/'+str(qna.id))
