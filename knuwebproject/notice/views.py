from django.shortcuts import render, redirect,get_object_or_404
from .models import Notice
from django.utils import timezone
from django.http import HttpResponse
import json
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, PageNotAnInteger
from next_prev import next_in_order, prev_in_order

# Create your views here.
def notice(request):
    notices = Notice.objects.all().order_by('-id')
    paginator = Paginator(notices, 10)
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1    
    

    posts = paginator.get_page(page)
    return render(request,"notice/notice.html",{'notices': posts})

def new(request):
    return render(request,'notice/new.html')

def create(request):
    notice = Notice()
    notice.title = request.GET['title']
    notice.body = request.GET['body']
    notice.pub_date = timezone.datetime.now()
    notice.save()
    return redirect("/notice/"+str(notice.id))

def detail(request,notice_id):
    notice = get_object_or_404(Notice,pk=notice_id)
    
    #맨 처음 글
    if(Notice.objects.first() == notice):
        prev = 0
    else:
        prev = prev_in_order(notice).id

    #맨 마지막 글
    if(Notice.objects.latest('id') == notice):
        next = 0
    else:
        next = next_in_order(notice).id

    return render(request,'notice/detail.html',{'notice':notice, 'prev':prev, 'next':next})

# def more(request):
#     pk = request.POST.get('pk',None)
#     notice = get_object_or_404(Notice, pk = pk)
    
#     # 돌려 보낼 때 모델 객체 자체를 보내지 말고, dict로 만들어서 보내라
#     # 모델 객체 자체를 보내려고 하면, 직렬화 error발생 하면서 힘들어짐 방법을 찾아야 할듯
#     ret = {
#         'body': notice.body,
#         'id': notice.id
#     }
#     # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"+str(notice)+"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#     return HttpResponse(json.dumps(ret), content_type="application/json")