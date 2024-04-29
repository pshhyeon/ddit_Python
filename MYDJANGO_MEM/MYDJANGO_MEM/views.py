from MYDJANGO_MEM.daomem import DaoMem
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

def main(request):
    return redirect('/mem_list')

def mem_list(request):
    dm = DaoMem()
    list = dm.selectList()
    return render(request, 'mem_list.html', {'list':list})

def mem_detail(request):
    m_id = request.GET['m_id']
    dm = DaoMem()
    vo = dm.selectOne(m_id)
    return render(request, 'mem_detail.html', {'vo':vo})

def mem_mod(request):
    m_id = request.GET['m_id']
    dm = DaoMem()
    vo = dm.selectOne(m_id)
    return render(request, 'mem_mod.html', {'vo':vo})

@csrf_exempt
def mem_mod_act(request):
    m_id = request.POST['m_id']
    m_name = request.POST['m_name']
    tel = request.POST['tel']
    email = request.POST['email']
    dm = DaoMem()
    cnt = dm.update(m_id, m_name, tel, email)
    return render(request, 'mem_mod_act.html', {'cnt':cnt})

def mem_add(request):
    return render(request, 'mem_add.html')

@csrf_exempt
def mem_add_act(request):
    m_id = request.POST['m_id']
    m_name = request.POST['m_name']
    tel = request.POST['tel']
    email = request.POST['email']
    dm = DaoMem()
    cnt = dm.insert(m_id, m_name, tel, email)
    return render(request, 'mem_add_act.html', {'cnt': cnt})

def mem_del_act(request):
    m_id = request.POST['m_id']
    dm = DaoMem()
    cnt = dm.delete(m_id)
    return render(request, 'mem_del_act.html', {'cnt': cnt})