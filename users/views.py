from  datetime import datetime

from django.shortcuts import render,HttpResponse

# Create your views here.
from users.models import User


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name+'---'+self.age

def index(request):
    name = '舒风'
    age = 18
    hobbys = ['Chi','wan','xue','shui']
    book = {'name':'放脱发指南','price':'50$'}
    stu = Student('yifei','23')
    data = {
        'name':name,
        'age':18,
        'hobbys':hobbys,
        'book':book,
        'stu':stu
    }
    return render(request,'users_index.html',context=data)


def test(request):
    msg = '<h3>shufeng is a good boy and lovely boy</h3>'
    number = 100
    score = 9.4567
    lists = ['饺子', '糖醋里脊', '干锅土豆片', '毛血旺', '溜肥肠']
    dt = datetime.now()
    data = {
        'msg':msg,
        'number':number,
        'score':score,
        'lists':lists,
        'dt':dt
    }
    return render(request,'test.html',context=data)

def tag_demo(request):
    list1 = [['饺子', '糖醋里脊', '干锅土豆片', '毛血旺', '溜肥肠'],
             ['可乐', '雪碧', '苏打水', '二锅头', '农夫山泉'],
             ['工体', '后海', '颐和园', '香山', '鸟巢']]
    lists = ['饺子', '糖醋里脊', '干锅土豆片', '毛血旺', '溜肥肠']
    return render(request, 'tag.html', context={'lists': lists, 'list1': list1})


def template_extends(request):
    return render(request,'welcome.html')

def include_demo(request):
    return render(request,'include_demo.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        if password == cpassword:
            user = User.objects.create(username=username, password=password, age=age, gender=gender, phone=phone)
            if user:
                return HttpResponse('注册成功')
            else:
                return render(request, 'login.html', context={'err': '注册失败'})
        else:
            return render(request, 'login.html',context={'err':'两次密码不一致'})
    return render(request,'login.html')