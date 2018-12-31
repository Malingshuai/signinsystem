from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    # return HttpResponse("Hello Word!")
    return render(request, "index.html")

def test(request):
    return render(request, "templates.html")

# 登录验证
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        # if username == "admin" and password == "admin123":
            request.session['user'] = username
            response = HttpResponseRedirect("/event_manage/")
            # response.set_cookie("user", username, 3600)
            return response
        else:
            return render(request, "index.html", {"error": "username error or password error!"})

# 发布会签到页面
@login_required
def event_manage(request):
    # username = request.COOKIES.get("user", "")
    username = request.session.get("user", "")
    return render(request, "event_manage.html", {"user": username})
