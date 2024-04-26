from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, 박박박")

def param(request):
    menu = request.GET['menu']
    return HttpResponse('PARAM : ' + menu) # f'PARAM : {menu}'

# 외부접근 허용 ==> @csrf_exempt
@csrf_exempt
def post(request):
    menu = request.POST.get('menu')
    return HttpResponse("POST : " + menu)

def forw(request):
    a = "홍길동"
    b = ["전우치", "변우석"]
    c = [
        {'e_id' : '1','e_name' : '1','gen' : '1','addr' : '1'},
        {'e_id' : '2','e_name' : '2','gen' : '2','addr' : '2'},
        {'e_id' : '3','e_name' : '3','gen' : '3','addr' : '3'}
        ]
    context = {'a':a , 'b':b, 'c':c}
    return render(request, 'forw.html', context)
