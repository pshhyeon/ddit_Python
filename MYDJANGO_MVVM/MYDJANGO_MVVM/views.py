from django.shortcuts import redirect, render
from django.http.response import HttpResponse
import base64

def index(request):
    return render(request, 'index.html')

def coo(request):
    return render(request, 'coo.html')

# session
def ses_in(request):
    request.session['e_id'] = '홍길동'
    request.session.set_expiry(15) #15초 동안 세션이 유효
    return HttpResponse("SES IN")

def ses_del(request):
    # del request.session['e_id'] # 특정 세션 삭제
    request.session.clear() # 세션 전체 삭제
    return HttpResponse("SES DEL")

def ses_view(request):
    # e_id = request.session['e_id']
    e_id = request.session.get('e_id', '') # e_id가 있으면 가져오고 없으면 ''
    return HttpResponse("SES VIEW<br>"+str(e_id))


# cookie
def coo_in(request):
    hr = HttpResponse("COO IN")
    
    # 한글을 쿠키에 넣을때 encoding 설정 필요
    # UTF-8 로 인코딩 하기 위한 base64 라이브러리를 사용
    # 성공 확인 후 주석처리함
    # encoding_data = base64.b64encode('홍길동'.encode()).decode()
    # hr.set_cookie('e_id', encoding_data)
    hr.set_cookie('e_id', 'aaaa')
    return hr

def coo_del(request):
    hr = HttpResponse("COO DEL")
    hr.delete_cookie('e_id')
    return hr

def coo_view(request):
    # e_id =''
    # try:
    #     e_id = request.COOKIES.get('e_id')
    # except : 
    #     e_id = ''
    
    # 한글을 쿠키에 가져올때도 decoding 설정 필요
    # 성공 확인 후 주석처리함
    e_id = request.COOKIES.get('e_id', '')
    # decoding_data = base64.b64decode(e_id).decode()
    return HttpResponse("COO VIEW <br>" + str(e_id))




