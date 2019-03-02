from django.shortcuts import render, get_object_or_404, redirect
from .models import QNA, Photo, Answer
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger
from next_prev import next_in_order, prev_in_order
from .forms import QNAForm
from django.db.models import Q

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

    ans = qna.answer_set.all()
    
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
    
    # 답변 달렸는지 여부
    # queryset의 empty 여부는 not으로 한다.
    if not ans:
        # print("@@@@@@@@@@@@@@@")
        c_ans = 0
        return render(request,'qna/detail.html',{'qna':qna, 'prev':prev, 'next':next, 'canEdit':canEdit, 'c_ans': c_ans})
    else:
        # print("!!!!!!!!!!!!!!!!!!!!")
        c_ans = 1
        return render(request,'qna/detail.html',{'qna':qna, 'prev':prev, 'next':next, 'canEdit':canEdit, 'ans':ans[0], 'c_ans': c_ans})
    

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

def search(request):
    query = request.GET['search']
    # kwds = QNA.objects.filter(title__icontains=query) | QNA.objects.filter(body__icontains=query)
    kwds = QNA.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).order_by('-id')
    paginator = Paginator(kwds, 10)

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    posts = paginator.get_page(page)
    return render(request, 'qna/search.html', {'kwds':posts})