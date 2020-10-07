from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app.models import User


def index(request):

    return render(request, 'index/首页.html')


def produce(request):

    return render(request, 'index/产品系列.html')


def recruitment(request):
    return render(request, 'index/人才招聘.html')


def teammember(request):
    return render(request, 'index/团队成员.html')


def service(request):
    return render(request, 'index/关于我们.html')


def contactus(request):
    return render(request, 'index/联系我们.html')


def solution(request):
    return render(request, 'index/解决方案.html')

def agri(request):
    return render(request, 'html/解决方案/agri.html')


def disaster(request):
    return render(request, 'html/解决方案/disaster.html')


def env(request):
    return render(request, 'html/解决方案/env.html')


def finance(request):
    return render(request, 'html/解决方案/finance.html')


def labor(request):
    return render(request, 'html/解决方案/labor.html')


def poverty(request):
    return render(request, 'html/解决方案/poverty.html')


def source(request):
    return render(request, 'html/解决方案/source.html')


def trade(request):
    return render(request, 'html/解决方案/trade.html')


def business_team(request):
    return render(request, 'html/团队成员/business_team.html')


def consultant_content(request):
    return render(request, 'html/团队成员/consultant_content.html')


def companyculture(request):
    return render(request, 'html/关于我们/公司文化.html')


def media(request):
    return render(request, 'html/关于我们/媒体引用.html')


def serviceobject(request):
    return render(request, 'html/关于我们/服务对象.html')


def simulation_platform(request):
    return render(request, 'html/产品系列/仿真平台.html')


def training_courses(request):
    return render(request, 'html/产品系列/培训课程.html')


def database(request):
    return render(request, 'html/产品系列/资料库.html')


def research_report(request):
    return render(request, 'html/产品系列/研究报告.html')


def simulation(request):
    return render(request, 'html/产品系列/仿真.html')


def peixun(request):
    return render(request, 'html/产品系列/培训.html')


def xinwen(request):
    return render(request, 'html/产品系列/新闻.html')


def yaniubaoao2(request):
    return render(request, 'html/产品系列/研究报告2.html')


def yaniubaoao3(request):
    return render(request, 'html/产品系列/研究报告3.html')


def yaniubaoao4(request):
    return render(request, 'html/产品系列/研究报告4.html')


def yaniubaoao5(request):
    return render(request, 'html/产品系列/研究报告5.html')


def yaniubaoao6(request):
    return render(request, 'html/产品系列/研究报告6.html')


def yaniubaoao7(request):
    return render(request, 'html/产品系列/研究报告7.html')


def yaniubaoao8(request):
    return render(request, 'html/产品系列/研究报告8.html')


def ziliao(request):
    return render(request, 'html/产品系列/资料.html')


def ruanjian(request):
    return render(request, 'html/产品系列/软件.html')


def registerinfo(request):
    return render(request, '管理端/平台管理/1.1个人注册信息.html')


def zhangmu(request):
    return render(request, '管理端/平台管理/2.1总账目查询.html')


def algorithm(request):
    return render(request, '管理端/平台管理/3.算法管理.html')


def userinfo(request):
    return render(request, '管理端/平台管理/4.1个人信息管理.html')


def algorithmusage(request):
    return render(request, '管理端/平台管理/5.1使用概况.html')


def price(request):
    return render(request, '管理端/平台管理/6.价格管理.html')

def register(request):

    if request.method=='GET':
        return render(request,'用户端/个人注册.html')
    elif request.method=="POST":

        username=request.POST.get("username")
        password=request.POST.get("password")
        field=request.POST.get("field")
        name=request.POST.get("name")
        org=request.POST.get("org")
        email=request.POST.get("email")
        password = make_password(password)

        user=User()
        user.userAccount=username
        user.userPasswd=password
        user.userField=field
        user.userName=name
        user.userOrganization=org
        user.userEmail=email

        user.save()

        return redirect(reverse('app:login'))

def login(request):
    if request.method == "GET":
        # error_message = request.session.get('error_message')
        data = {
            "title": "登录"
        }
        # if error_message:
        #     del request.session['error_message']
        #     data['error_message'] = error_message
        return render(request, '用户端/登录.html', context=data)

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        users = User.objects.filter(userAccount=username)
        if users.exists():
            user = users.first()
            if check_password(password, user.userPasswd):
                    request.session['user_id'] = user.id
                    return redirect(reverse('app:index'))
            else:
                print('密码错误')
                # request.session['error_message'] = 'password error'
                return redirect(reverse('app:login'))
        print('用户不存在')
        # request.session['error_message'] = 'user does not exist'
        return redirect(reverse('app:login'))



def checkuser(request):
    username = request.GET.get("username")
    users = User.objects.filter(userAccount=username)
    data = {
        "status": 200,
        "msg": 'user can use'
    }
    if users.exists():
        data['status'] = 901
        data['msg'] = 'user already exist'
    else:
        pass
    return JsonResponse(data=data)




def a(request):
    return render(request, '用户端/new.html')


def register2(request):
    if request.method == 'GET':
        return render(request, '用户端/团队注册.html')
    else:
        return render(request, '用户端/团队注册.html')