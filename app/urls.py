from django.conf.urls import url

from app import views
app_name='app'


urlpatterns = [
    # 首页
    url(r'^index/', views.index, name='index'),

    # 关于我们
    url(r'^aboutus/', views.service, name='aboutus'),
    # 关于我们文件夹
    url(r'^companyculture/', views.companyculture, name='companyculture'),
    url(r'^media/', views.media, name='media'),
    url(r'^serviceobject/', views.serviceobject, name='serviceobject'),

    # 团队成员
    url(r'^teammember/', views.teammember, name='teammember'),
    # 团队成员文件夹
    url(r'^business_team/', views.business_team, name='business_team'),
    url(r'^consultant_content/', views.consultant_content, name='consultant_content'),

    # 解决方案
    url(r'^solution/', views.solution, name='solution'),
    # 解决方案文件夹
    url(r'^agri/', views.agri, name='agri'),
    url(r'^disaster/', views.disaster, name='disaster'),
    url(r'^env/', views.env, name='env'),
    url(r'^finance/', views.finance, name='finance'),
    url(r'^labor/', views.labor, name='labor'),
    url(r'^poverty/', views.poverty, name='poverty'),
    url(r'^source/', views.source, name='source'),
    url(r'^trade/', views.trade, name='trade'),

    # 产品系列
    url(r'^produce/', views.produce, name='produce'),
    # 产品系列文件夹
    url(r'^simulation/', views.simulation, name='simulation'),
    url(r'^simulation_platform/', views.simulation_platform, name='simulation_platform'),
    url(r'^training_courses/', views.training_courses, name='training_courses'),
    url(r'^database/', views.database, name='database'),
    url(r'^research_report/', views.research_report, name='research_report'),
    url(r'^peixun/', views.peixun, name='peixun'),
    url(r'^xinwen/', views.xinwen, name='xinwen'),
    url(r'^yanjiubaogao2/', views.yaniubaoao2, name='yanjiubaogao2'),
    url(r'^yanjiubaogao3/', views.yaniubaoao3, name='yanjiubaogao3'),
    url(r'^yanjiubaogao4/', views.yaniubaoao4, name='yanjiubaogao4'),
    url(r'^yanjiubaogao5/', views.yaniubaoao5, name='yanjiubaogao5'),
    url(r'^yanjiubaogao6/', views.yaniubaoao6, name='yanjiubaogao6'),
    url(r'^yanjiubaogao7/', views.yaniubaoao7, name='yanjiubaogao7'),
    url(r'^yanjiubaogao8/', views.yaniubaoao8, name='yanjiubaogao8'),
    url(r'^ziliao/', views.ziliao, name='ziliao'),
    url(r'^ruanjian/', views.ruanjian, name='ruanjian'),

    #人才招聘
    url(r'^recruitment/', views.recruitment, name='recruitment'),

    #联系我们
    url(r'^contactus/', views.contactus, name='contactus'),





    url(r'^registerinfo/', views.registerinfo, name='registerinfo'),
    url(r'^zhangmu/', views.zhangmu, name='zhangmu'),
    url(r'^algorithm/', views.algorithm, name='algorithm'),
    url(r'^userinfo/', views.userinfo, name='userinfo'),
    url(r'^algorithmusage/', views.algorithmusage, name='algorithmusage'),
    url(r'^price/', views.price, name='price'),



    url(r'^register/', views.register, name='register'),
    url(r'^register2/', views.register2, name='register2'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^checkuser/', views.checkuser, name='checkuser'),
    url(r'^checkmanager/', views.checkmanager, name='checkmanager'),
    url(r'^personcenter/', views.personcenter, name='personcenter'),
    url(r'^personcenter2/', views.personcenter2, name='personcenter2'),


    url(r'^algorithmcall/', views.algorithmcall, name='algorithmcall'),




]
