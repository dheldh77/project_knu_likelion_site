from django.shortcuts import render, get_object_or_404, redirect
from .models import QNA, Photo, Answer
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger
from next_prev import next_in_order, prev_in_order
from .forms import QNAForm

# Create your views here.
def qna(request):
    qnas = QNA.objects.all().order_by('-id')
    paginator = Paginator(qnas, 10)

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    posts = paginator.get_page(page)
    
    return render(request,'qna/qna.html', {'qnas':posts})

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

def new(request):
    return render(request,'qna/new.html')

def detail(request, qna_id):
    qna = get_object_or_404(QNA,pk=qna_id)

    #맨 처음 글
    if(QNA.objects.first() == qna):
        prev = 0
    else:
        prev = prev_in_order(qna).id

    #맨 마지막 글
    if(QNA.objects.last() == qna):
        next = 0
    else:
        next = next_in_order(qna).id
    
    if (qna.user == request.user):
        canEdit = True
    else:
        canEdit = False
    
    return render(request,'qna/detail.html',{'qna':qna, 'prev':prev, 'next':next, 'canEdit':canEdit})

def delete(request, qna_id):
    get_object_or_404(QNA, pk=qna_id).delete()

    return redirect('/qna/')

def edit(request, qna_id):
    post = get_object_or_404(QNA, pk=qna_id)
    return render(request, 'qna/edit.html', {'post':post})

def update(request, qna_id):
    qna = get_object_or_404(QNA, pk=qna_id)
    qna.title = request.POST['title']
    qna.body = request.POST['body']
    qna.save()
    return redirect('/qna/'+str(qna.id))

def ans(request, ans_id):
    ans = get_object_or_404(Answer, pk=ans_id)

    return render(request,'qna/ans.html',{'ans':ans})

# FORM 태그 활용 QNA
def newQNA(request):
    # 입력된 내용 처리 -> POST
    if request.method == 'POST':
        form = QNAForm(request.POST)
        if form.is_valid(): # 잘입력된지 체크
            qna = form.save(commit=False)
            qna.user= request.user
            qna.pub_date = timezone.now()
            qna.save() # 저장하기
            return redirect('/qna/'+str(qna.id)) 
    

    # 빈 페이지 띄워주는 기능 -> GET
    else :
        form = QNAForm()
        return render(request, 'qna/new.html', {'form':form})

def editQNA(request, qna_id):
    # 객체 가져오기
    qna = get_object_or_404(QNA, pk=qna_id)
    
    # 입력된 내용 처리 -> POST
    if request.method == 'POST':
        form = QNAForm(request.POST or None, instance=qna)
        if form.is_valid(): # 잘입력된지 체크
            post = form.save(commit=False)
            post.save() # 저장하기
            return redirect('/qna/'+str(qna.id))
    

    # 빈 페이지 띄워주는 기능 -> GET
    else :
        form = QNAForm(instance=qna)
        return render(request, 'qna/edit.html', {'qna':qna,'form':form})