from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.http import HttpResponseRedirect

# Create your views here.

# table
from .models import Travel

def info_demo(request):
    if request.user.has_perm('demo2.a2'):
        t1 = Travel.objects.get(pk=1)
        t_demo = {'info': t1}
        return render(request, 'table_info.html', t_demo)
    else:
        return HttpResponseRedirect('/list/')

from django.contrib.auth.decorators import permission_required
@permission_required('demo2.a1', login_url='/list/')
def table_info(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    t_info = {'info': travel}
    return render(request, 'table_info.html', t_info)

from django.contrib.auth.decorators import login_required
@login_required(login_url='/')
def table_list(request):
    travel = Travel.objects.all()
    t_list = {'travels': travel}
    return render(request, 'table_list.html', t_list)

from .forms import CreateForm, CreateModelForm
from .models import Location
from django.contrib import messages #alert

def table_create(request):
    # Form
    if 'f' in request.POST: #接收到post
        form = CreateForm(request.POST or None) #取得表單
        if form.is_valid(): #驗證表單
            info = form.cleaned_data #取得數值
            try:
                # 新增全部
                #Location.objects.create(**info)
                # 限定新增項目
                Location.objects.create(
                    id_location=info['id_location'],
                    country=info['country'], 
                    city='瓦干達', #自訂
                )
                messages.success(request, 'Create Successful !')
            except:
                messages.error(request, 'Create Failed !')
            #form = CreateForm() #清空
            return HttpResponseRedirect('/create/') #避免F5後重新輸入
    else:
        form = CreateForm() #初始化
    
    # ModelForm
    if 'mf' in request.POST:
        modelform = CreateModelForm(request.POST or None)
        if modelform.is_valid():
            # 新增全部方法1
            #Location.objects.create(**modelform.cleaned_data)
            # 新增全部方法2
            modelform.save()
            return HttpResponseRedirect('/create/') #避免F5後重新輸入
    else:
        modelform = CreateModelForm() #初始化

    # return
    context = {'form':form, 'modelform':modelform}
    return render(request, 'table_create.html', context)

    
# login
def login(request):    
    if request.user.is_authenticated: #已登入
        return HttpResponseRedirect('/list/') #跳轉頁面
    else:
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        user = auth.authenticate(username=username, password=password) #輸入帳密
        if user is not None and user.is_active: #帳號存在
            auth.login(request, user) #登入
            return HttpResponseRedirect('/list/') #成功級即跳轉
        else:
            return render(request, 'login.html')

from .forms import LoginForm
def login_forms(request):
    form = LoginForm()
    context = {
        'login_form': form
    }
    if request.user.is_authenticated: #已登入
        return HttpResponseRedirect('/list/') #跳轉頁面
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password) #輸入帳密
        if user is not None and user.is_active: #帳號存在
            auth.login(request, user) #登入
            return HttpResponseRedirect('/list/') #成功級即跳轉
        else:        
            return render(request, 'login_forms.html', context)

# logout
def logout(request):
    auth.logout(request) #登出
    return HttpResponseRedirect('/') #跳回登入頁面

# signup
from .forms import SignupForm
from django.contrib.auth.models import User
from .models import VerifyCode
import hashlib
import datetime
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from smtplib import SMTPException
'''
def signup(request): #無註冊碼
    if request.method == 'POST':
        form = SignupForm(request.POST or None) #取得表單
        if form.is_valid(): #驗證表單
            ### 註冊未啟用帳號 ###
            info = form.cleaned_data #取得數值
            form.save() #密碼演算法問題,不能用ORM的Create
            new_user = User.objects.filter(username=info['username'])
            new_user.update(is_active=False) #預設帳號不啟用

            ### 寄信功能 by SMTP ###
            email_context = str(info['username'])+'，您好：\n註冊成功，\n請啟用帳號！'
            email = EmailMessage(
                '<Django> 帳號驗證', #電子郵件標題
                email_context, #電子郵件內容
                settings.EMAIL_HOST_USER, #寄件者
                [info['email'],'joe82512@gmail.com'] #收件者/副本
            )         
            email.fail_silently = False #觸發smtplib.SMTPException            
            try:
                email.send()                
                messages.success(request, '註冊成功，請至信箱啟用帳號')
            except SMTPException as e: #SMTP功能失效
                new_user.delete() #刪掉註冊帳號
                msg = 'SMTP Error:' + str(e) #失效訊息
                messages.error(request, msg)
            except:
                new_user.delete() #刪掉註冊帳號
                messages.error(request, '註冊失敗：無法寄送信件，請檢查信箱是否正確')
            
            return HttpResponseRedirect('/signup/') #避免F5後重新輸入        
        
        else:
            messages.error(request, '註冊失敗')
    
    else:
        form = SignupForm() #初始化

    # return
    context = {'signup_form': form}
    return render(request, 'signup.html', context)
'''

# 驗證碼
def hash_code(s, salt='0'): #產生驗證碼
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def make_verify(user): #驗證碼與User連結的資料表
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.username, now)
    return code

def verify_time(user): #比對驗證時間
    c_time = user.c_time.replace(tzinfo=None) #驗證碼產生時間
    now = datetime.datetime.utcnow() #點擊連結時間
    nc = now - c_time #計算時間差
    nc = nc.total_seconds() #轉成秒數float
    return nc

def del_expired_user(): #刪除過期的使用者帳號及驗證碼
    VC = VerifyCode.objects.all()
    for v in VC:
        if (verify_time(v)>600): v.user.delete()
    print('clear!')

# 註冊信
def signup(request):
    del_expired_user() #刪除過期的使用者帳號
    if request.method == 'POST':
        form = SignupForm(request.POST or None) #取得表單
        if form.is_valid(): #驗證表單
            ### 註冊未啟用帳號 ###
            info = form.cleaned_data #取得數值
            form.save() #密碼演算法問題,不能用ORM的Create
            new_user = User.objects.filter(username=info['username'])
            new_user.update(is_active=False) #預設帳號不啟用
            n1 = new_user[0]
            code = make_verify(n1)
            VerifyCode.objects.create(code=code, user=n1,)

            ### 寄信功能 by SMTP ###
            # 信件1: 純文字版(html失敗時替代)
            code_url = 'http://'+'127.0.0.1:8000'+'/verification/?code='+code
            email_context = str(info['username'])+'，您好：\n註冊成功，\n請點擊連結啟用帳號，\n'+code_url+'\n連結將在10分鐘後失效。'    
            # 信件2: html版本
            html_content = '''
                <p>{}，您好：</p>
                <p>註冊成功，</p>
                <p>請點擊<a href="http://{}/verification/?code={}">連結</a>啟用帳號，</p>
                <p>連結將在10分鐘後失效。</p>
                '''.format(str(info['username']), '127.0.0.1:8000', code)
            # 信件打包及設定
            email = EmailMultiAlternatives(
                '<Django> 帳號驗證', #電子郵件標題
                email_context, #電子郵件內容
                settings.EMAIL_HOST_USER, #寄件者
                [info['email'],'joe82512@gmail.com'] #收件者/副本
            )
            email.attach_alternative(html_content, 'text/html')

            # 寄送
            email.fail_silently = False #觸發smtplib.SMTPException
            try:
                email.send()
                messages.success(request, '註冊成功，請至信箱啟用帳號')
            except SMTPException as e: #SMTP功能失效
                new_user.delete() #刪掉註冊帳號
                msg = 'SMTP Error:' + str(e) #失效訊息
                messages.error(request, msg)                
            except:
                new_user.delete() #刪掉註冊帳號
                messages.error(request, '註冊失敗：無法寄送信件，請檢查信箱是否正確')
            
            return HttpResponseRedirect('/signup/') #避免F5後重新輸入  
        
        else: #表單驗證失敗
            messages.error(request, '註冊失敗')
    
    else: #未收到POST
        form = SignupForm() #初始化

    # return
    context = {'signup_form': form}
    return render(request, 'signup.html', context)



# 驗證碼連結
def verification(request):
    code = request.GET.get('code', None) #get
    try:
        confirm = VerifyCode.objects.get(code=code) #比對驗證碼
    except:
        msg = '驗證連結已失效'
        return render(request, 'verify.html', {'code':code,'msg':msg})

    nc = verify_time(confirm) #驗證時間差
    if nc < 600:
        User.objects.filter(id=confirm.user.pk).update(is_active=True) #啟用帳號
        msg = '驗證成功，請登入帳號！'
    else: 
        user = User.objects.filter(id=confirm.user.pk)
        user.delete() #刪除使用者帳號
        msg = '驗證碼已過期，請重新註冊！'

    confirm.delete() #刪除驗證碼    
    return render(request, 'verify.html', {'code':code,'msg':msg})


# password reset
from django.contrib.auth.views import PasswordResetView
from .forms import NewPasswordResetForm
class NewPasswordResetView(PasswordResetView):
    form_class = NewPasswordResetForm


### advance ###
from .models import Food, Drink, Restaurant, City
from django.db.models import F, Q #Querny對象
from functools import reduce
from operator import or_, and_ #Querny邏輯運算
def food(request):
    # F對象
    #food = Food.objects.all().annotate(unit_price=F('price')/F('quantity'))
    # Q對象
    food = Food.objects.filter(Q(name__contains='蛋') | Q(name__contains='雞'))
    '''
    food = Food.objects.filter(name__contains='蛋')
    food = food | Food.objects.filter(name__contains='雞')
    '''
    food = food.annotate(unit_price=F('price')/F('quantity'))
    return render(request, 'food_list.html', {'foods': food})

def search_food(request):
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        if keywords != '':            
            keyword_list = keywords.split() #空白分割
            Q_list = reduce(or_, (Q(name__contains=keyword) for keyword in keyword_list))
            food = Food.objects.filter(Q_list)
            food = backward_search(food, Q_list) #反向查詢
            food = food.annotate(unit_price=F('price')/F('quantity'))
        else: #無關鍵字
            food = Food.objects.none()
    else: #初始化
        food = Food.objects.none()
        keywords = ''
    return render(request, 'food_list.html', {'key':str(keywords),'foods':food})

def backward_search(food, Q_list):
    drink_list = Drink.objects.filter(Q_list)
    for d in drink_list:
        f = d.food_set.all()
        food = food | f
    restaurant_list = Restaurant.objects.filter(Q_list)
    for r in restaurant_list:
        f = r.food_set.all()
        food = food | f
    return food

def related_food(request):
    ### 正向查詢 ###
    #food = Food.objects.all()
    #food = Food.objects.select_related('drink').select_related('restaurant').select_related('restaurant__city').all()
    food = Food.objects.select_related('restaurant__city').filter(restaurant__city__name__contains='高雄')
    
    ### 反向查詢 ###
    '''
    food = Food.objects.none()
    city_list = City.objects.filter(name__contains='高雄')
    for c in city_list:
        restaurant_list = c.restaurant_set.all()
        for r in restaurant_list:
            f = r.food_set.all()
            food = food | f
    '''
    
    '''
    food = Food.objects.none()
    city_list = City.objects.prefetch_related('restaurant_set').filter(name__contains='高雄')
    for c in city_list:
        restaurant_list = c.restaurant_set.all()
        for r in restaurant_list:
            f = r.food_set.all()
            food = food | f
    '''
    food = food.annotate(unit_price=F('price')/F('quantity'))
    return render(request, 'food_list.html', {'foods': food})


### AJAX ###
from django.http import HttpResponse
import json
def key_search(food, keyword_list):
    food = Food.objects.filter(reduce(or_, (Q(name__contains=keyword) for keyword in keyword_list)))
    # drink search
    f = Food.objects.select_related('drink').filter(reduce(or_, (Q(drink__name__contains=keyword) for keyword in keyword_list)))
    food = food | f
    # restaurant search
    f = Food.objects.select_related('restaurant').filter(reduce(or_, (Q(restaurant__name__contains=keyword) for keyword in keyword_list)))
    food = food | f
    # city search
    f = Food.objects.select_related('restaurant__city').filter(reduce(or_, (Q(restaurant__city__name__contains=keyword) for keyword in keyword_list)))
    food = food | f
    food = food.order_by('pk')
    f_idx = food.values('id')
    return f_idx

def data_page(request):
    global keys #for data_ajax
    if request.method == 'POST':
        keys = request.POST.get('keywords')
    else: #初始化
        keys = ''
    return render(request, 'food_ajax.html', {'key':str(keys)})

def data_ajax(request):
    if request.method == 'POST':
        food = Food.objects.none()
        if keys != '':
            keyword_list = keys.split() #空白分割
            f_idx = key_search(food, keyword_list)
            food = Food.objects.select_related('drink').select_related('restaurant').select_related('restaurant__city').filter(pk__in=f_idx)
        food_list = []
        for fd in food:
            food_list.append({
                'name': fd.name,
                'price': fd.price,
                'quantity': fd.quantity,
                'unit_price': fd.price/fd.quantity,
                'drink': fd.drink.name,
                'restaurant': fd.restaurant.name,
                'city': fd.restaurant.city.name,
            })
        return HttpResponse(json.dumps(food_list), content_type="application/json")

def count_ajax(request):
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        food = Food.objects.none()
        if keywords != '':
            keyword_list = keywords.split() #空白分割
            count = len(key_search(food, keyword_list))
        else:
            count = 0
        return HttpResponse(json.dumps({"count":count}), content_type="application/json")