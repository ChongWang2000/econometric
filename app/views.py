from django.http import  HttpResponse
from django.shortcuts import render

# Create your views here.
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