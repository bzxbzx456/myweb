from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
    <style>
        div{
            width: 200px;
            height: 200px;
            border: 1px solid red;
        }
    </style>
</head>
<body>
    <h1>woaini</h1>
    <div></div>
</body>
</html>
    '''
    return HttpResponse(html)

def index1(request):
    print(request.get_host())
    return HttpResponse('hello world')

def index2(request):
    return HttpResponse('55555')

def index3(request):
    return render(request,'index.html')