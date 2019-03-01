from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        passwd = request.POST['passwd']
        user = auth.authenticate(request,username=user_id,password=passwd)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,"login.html",{'error':'유저 ID 혹은 password가 잘못되었습니다.', 'status': 0})
    else:
        return render(request,"login.html", {'status': 1})

def signup(request):
    if request.method == "POST":
        if not User.objects.filter(username=request.POST['user_id']).exists() :
            if request.POST['passwd1'] == request.POST['passwd2']:
                user = User.objects.create_user(username=request.POST['user_id'], password=request.POST['passwd1'])
                auth.login(request, user)
                return redirect('home')
            else :
                return render(request, "signup.html",{"error":"비밀 번호가 일치하지 않습니다.", "status": 1})
        else :
            return render(request, "signup.html",{"error":"이미 존재하는 ID입니다.", "status": 1})
    return render(request,"signup.html", {"status":0})

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request,'login.html')

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