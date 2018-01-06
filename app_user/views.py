from django.shortcuts import render, redirect
from hashlib import sha1
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import UserInfo, UserAddress, BrowseHistory
from app_goods.models import GoodsInfo
from . import user_decorator
from app_cart.models import OrderInfo, OrderDetailInfo
# Create your views here.


def register(request):
    return render(request, 'app_user/register.html')


def register_handle(request):
    uname = request.POST['user_name']
    upwd = request.POST['pwd']
    uemail = request.POST['email']
    m = sha1()
    m.update(upwd.encode())
    upwd2 = m.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd2
    user.uemail = uemail
    user.save()
    return redirect('/user/login')


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'uname': uname, 'pwd_error': 0, 'user_error': 0}
    return render(request, 'app_user/login.html', context=context)


def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    remember = post.get('remember')
    user_error = 0
    pwd_error = 0
    filt = UserInfo.objects.filter(uname=uname)

    if len(filt) == 0:
        #  true: user not exist
        user_error = 1
    else:
        m = sha1()
        m.update(upwd.encode())
        pwd_encrypt = m.hexdigest()
        rec = filt[0]
        if rec.upwd == pwd_encrypt:
            url = request.COOKIES.get('url', '/goods/index')
            response = HttpResponseRedirect(url)
            response.set_cookie('uid', filt[0].id)
            request.session['user_id'] = filt[0].id
            request.session['user_name'] = uname
            #  if password correct save user name
            if remember == 1:
                response.set_cookie('uname', uname)
            else:
                response.set_cookie('uname', '', max_age=-1)

            return response
        else:
            pwd_error = 1
    context = {'uname': uname, 'pwd_error': pwd_error, 'user_error': user_error}
    return render(request, 'app_user/login.html', context=context)


def query_user(request):
    # query user is exist
    uname = request.GET.get('uname')    #  use get will not make exception
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


@user_decorator.login
def user_center_info(request):
    # uid = request.COOKIES.get('uid', '')
    uid = request.session.get('user_id')
    user = UserInfo.objects.filter(id=2)
    #  user if have login
    if len(user) == 0:
        return redirect('/user/login')
    else:
        browser_goods = []
        historys = BrowseHistory.objects.filter(uid=uid).order_by('-id')
        if len(historys) > 6:
            historys = historys[0:6]

        for history in historys:
            one_goods = history.gid
            browser_goods.append(one_goods)

        addresses = UserAddress.objects.filter(user_id=uid)
        if len(addresses) > 0:
            address = addresses[0].address
        else:
            address = ''
        context = {'uname':user[0].uname, 'uphone':user[0].uphone, 'uaddress':address,
                   'browser_goods':browser_goods}
        return render(request, 'app_user/user_center_info.html', context=context)


@user_decorator.login
def user_center_order(request):
    uid = request.session.get('user_id')
    orders = OrderInfo.objects.filter(uid=uid)
    orders_details = []
    for order in orders:
        detail = order.orderdetailinfo_set.all()
        orders_details.append([order, detail])

    context = {'orders_details':orders_details}  # order_detail = [ [order, [detail]  ] , [order, [detail]  ]

    return render(request, 'app_user/user_center_order.html', context=context)


@user_decorator.login
def user_center_site(request):
    uid = request.session.get('user_id')

    user = UserInfo.objects.get(id=uid)
    # get the latest address
    address = user.useraddress_set.order_by('-id')[0]

    context = {'address':address}
    return render(request, 'app_user/user_center_site.html', context=context)


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/goods/index')

def revise_address(request):
    post = request.POST
    uid = request.session.get('user_id')
    address = UserAddress.objects.get(user=uid)
    address.recipient = post.get('recipient')
    address.address = post.get('address')
    address.rphone = post.get('rphone')
    address.rcode = post.get('rcode')
    address.save()
    return redirect('/user/site')