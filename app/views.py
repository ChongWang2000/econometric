from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app.models import User, Team


def index(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'index/首页.html', context=data)


def produce(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'index/产品系列.html',data)


def recruitment(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'index/人才招聘.html',data)


def teammember(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'index/团队成员.html',data)


def service(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'index/关于我们.html',data)


def contactus(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'index/联系我们.html',data)


def solution(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True
    return render(request, 'index/解决方案.html',data)

def agri(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/解决方案/agri.html',data)


def disaster(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/解决方案/disaster.html',data)


def env(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/解决方案/env.html',data)


def finance(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/解决方案/finance.html',data)


def labor(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/解决方案/labor.html',data)


def poverty(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/解决方案/poverty.html',data)


def source(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/解决方案/source.html',data)


def trade(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/解决方案/trade.html',data)


def business_team(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/团队成员/business_team.html',data)


def consultant_content(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/团队成员/consultant_content.html',data)


def companyculture(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/关于我们/公司文化.html',data)


def media(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/关于我们/媒体引用.html',data)


def serviceobject(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/关于我们/服务对象.html',data)


def simulation_platform(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/仿真平台.html',data)


def training_courses(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/培训课程.html',data)


def database(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/资料库.html',data)


def research_report(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/研究报告.html',data)


def simulation(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/仿真.html',data)


def peixun(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/培训.html',data)


def xinwen(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/新闻.html',data)


def yaniubaoao2(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/研究报告2.html',data)


def yaniubaoao3(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/研究报告3.html',data)


def yaniubaoao4(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/研究报告4.html',data)


def yaniubaoao5(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/研究报告5.html',data)


def yaniubaoao6(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/研究报告6.html',data)


def yaniubaoao7(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/研究报告7.html',data)


def yaniubaoao8(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/研究报告8.html',data)


def ziliao(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/资料.html',data)


def ruanjian(request):
    user_id = request.session.get('user_id')
    team_id = request.session.get('team_id')
    data = {
        'is_login': False,
        'is_personal': False,
        'is_team': False,
    }
    if user_id:
        data['is_login'] = True
        data['is_personal'] = True

    elif team_id:
        data['is_login'] = True
        data['is_team'] = True

    return render(request, 'html/产品系列/软件.html',data)


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
        phone=request.POST.get("phone")
        password = make_password(password)

        user=User()
        user.userAccount=username
        user.userPasswd=password
        user.userField=field
        user.userName=name
        user.userOrganization=org
        user.userEmail=email
        user.userPhone=phone

        user.save()

        return redirect(reverse('app:login'))

def register2(request):
    if request.method == 'GET':
        return render(request, '用户端/团队注册.html')
    else:
        username=request.POST.get("username")
        password=request.POST.get("password")
        field=request.POST.get("field")
        name=request.POST.get("name")

        users = User.objects.filter(userAccount=username)
        user=users.first()

        password = make_password(password)

        team=Team()
        team.managerAccount=user.userAccount
        team.managerName=user.userName
        team.managerOrganization=user.userOrganization
        team.managerEmail=user.userEmail
        team.managerPhone=user.userPhone
        team.teamPasswd=password
        team.teamField=field
        team.teamName=name
        team.save()


        return redirect(reverse('app:login'))


def login(request):
    if request.method == "GET":
        data = {
            "title": "登录"
        }
        return render(request, '用户端/登录.html', context=data)

    elif request.method == "POST":
        check_box_list = request.POST.getlist('boxes')
        # if check_box_list:
        #     print(check_box_list)
        #     return HttpResponse("ok")
        # else:
        #     print("fail")
        #     return HttpResponse("fail")

        if check_box_list[0]=='个人用户':
            username = request.POST.get("username")
            password = request.POST.get("password")
            users = User.objects.filter(userAccount=username)
            if users.exists():
                user = users.first()
                if check_password(password, user.userPasswd):
                    request.session['user_id'] = user.id
                    return redirect(reverse('app:personcenter'))
                else:
                    print('密码错误')
                    # request.session['error_message'] = 'password error'
                    return redirect(reverse('app:login'))
        elif check_box_list[0]=='团队用户' :
            username = request.POST.get("username")
            password = request.POST.get("password")
            teams=Team.objects.filter(managerAccount=username)
            if teams.exists():
                team = teams.first()
                if check_password(password, team.teamPasswd):
                    request.session['team_id'] = team.id
                    return redirect(reverse('app:personcenter2'))
                else:
                    print('密码错误')
                    # request.session['error_message'] = 'password error'
                    return redirect(reverse('app:login'))
        else:
            print('用户不存在')
            # request.session['error_message'] = 'user does not exist'
            return redirect(reverse('app:login'))





def logout(request):
    request.session.flush()

    return redirect(reverse('app:index'))




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

def checkmanager(request):
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


def personcenter(request):

    user_id = request.session.get('user_id')

    data = {
        'is_login': False
    }

    if user_id:
        user = User.objects.get(pk=user_id)
        data['is_login'] = True
        data['username'] = user.userAccount
        data['name'] = user.userName
        data['email'] = user.userEmail
        data['field'] = user.userField
        data['organization'] = user.userOrganization

    return render(request, '用户端/个人中心.html', context=data)


def personcenter2(request):
    team_id = request.session.get('team_id')

    data = {
        'is_login': False
    }

    if team_id:
        team = Team.objects.get(pk=team_id)
        data['is_login'] = True
        data['name'] = team.teamName
        data['email'] = team.managerEmail
        data['field'] = team.teamField
        data['organization'] = team.managerOrganization

    return render(request, '用户端/团队中心.html', context=data)



def algorithmcall(request):
    team_id = request.session.get('team_id')
    user_id = request.session.get('user_id')
    data = {
        'is_login': False,
        'is_personal':False,
        'is_team':False,
    }
    if user_id:
        user = User.objects.get(pk=user_id)
        data['is_login'] = True
        data['is_personal']=True
        return render(request, '用户端/new.html', data)
    elif team_id:
        team = Team.objects.get(pk=team_id)
        data['is_login'] = True
        data['is_team']=True
        return render(request, '用户端/new.html', data)