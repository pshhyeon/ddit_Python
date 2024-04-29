from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
import pymysql
from django.urls.base import reverse
from MYDJANGO_MVC.daoemp import DaoEmp

def main(request):
    # 상대 경로
    return redirect('/emp_list')
    # 절대경로
    # return redirect('http://127.0.0.1:8000/emp_list')

# 내가 했던 코드
def mine_emp_list(request):
    con = pymysql.connect(host='localhost'
                          , port = 3305
                          , user='root'
                          , password='python'
                          , db='python'
                          , charset='utf8')
    
    cur = con.cursor(pymysql.cursors.DictCursor)
    
    sql = """
        select 
            e_id, e_name, gen, addr 
        from emp
    """
    
    cur.execute(sql)
    list = cur.fetchall()
    print(list)
    
    cur.close()
    con.close()
    
    return render(request, 'emp_list.html', {'list':list})

# 수업때 했던 코드 ==> dao생성
def emp_list(request):
    de = DaoEmp()
    list = de.selectList()
    return render(request, 'emp_list.html', {'list':list})

def emp_detail(request):
    e_id = request.GET['e_id']
    de = DaoEmp()
    vo = de.selectOne(e_id)
    return render(request, 'emp_detail.html', {'vo':vo})

def emp_mod(request):
    e_id = request.GET['e_id']
    de = DaoEmp()
    vo = de.selectOne(e_id)
    return render(request, 'emp_mod.html', {'vo':vo})

@csrf_exempt
def emp_mod_act(request):
    e_id = request.POST.get('e_id')
    e_name = request.POST.get('e_name')
    gen = request.POST.get('gen')
    addr = request.POST.get('addr')
    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)
    return render(request, 'emp_mod_act.html', {'cnt': cnt})

def emp_add(request):
    return render(request, 'emp_add.html')

@csrf_exempt
def emp_add_act(request):
    e_id = request.POST['e_id']
    e_name = request.POST['e_name']
    gen = request.POST['gen']
    addr = request.POST['addr']
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    return render(request, 'emp_add_act.html', {'cnt': cnt})

@csrf_exempt
def emp_del_act(request):
    e_id = request.GET['e_id']
    de = DaoEmp()
    cnt = de.delete(e_id);
    return render(request, 'emp_del_act.html', {'cnt': cnt})




