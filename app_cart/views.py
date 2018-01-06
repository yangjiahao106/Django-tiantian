from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from app_user import user_decorator
from .models import Cart, OrderInfo, OrderDetailInfo
from app_user.models import UserInfo, UserAddress
from app_goods.models import GoodsInfo
from django.db import transaction
import datetime

# Create your views here.

@user_decorator.login
def mycart(request):
    uid = request.session.get('user_id')
    cart = Cart.objects.filter(uid=uid)

    context = {'cart': cart}

    return render(request, 'app_cart/cart.html', context=context)


@user_decorator.login
def add_cart(request, gid, gnumber):
    uid = request.session.get('user_id')
    gid = int(gid)
    gnumber = int(gnumber)
    cart = Cart.objects.filter(uid=uid, gid=gid)
    if len(cart) == 0:
        one = Cart()
        one.uid_id = uid
        one.gid_id = gid
        one.gnumber = gnumber
        one.save()
    else:
        cart[0].gnumber +=  gnumber
        cart[0].save()

    return HttpResponseRedirect('/cart/mycart')


def updata_cart(request):
    uid = int( request.session.get('user_id') )
    gid = int( request.GET.get('gid') )
    gnumber = int(request.GET.get('gnumber') )
    cart = Cart.objects.filter(uid_id=uid, gid_id=gid)
    cart = cart[0]
    print('*****cart id',cart.id, 'gnumer', gnumber ,'gid', gid)
    if gnumber == 0:
        cart.delete()
    else:
        cart.gnumber = gnumber
        cart.save()

    return JsonResponse({'gnumber': gnumber})


def update_select(request):
    uid = int(request.session.get('user_id'))
    gid = int(request.GET.get('gid'))
    is_select = request.GET.get('isselect')
    if is_select == 'true':
        is_select = 1
    else:
        is_select = 0
    print('*****cart id', 'is_select', type(is_select))
    if gid == -1:
        cart = Cart.objects.filter(uid_id=uid)
        for one in cart:
            one.isselect = is_select
            one.save()
    else:
        cart = Cart.objects.filter(uid_id=uid, gid_id=gid)
        cart = cart[0]
        cart.isselect = is_select
        cart.save()

    return JsonResponse({'hello':1})


@user_decorator.login
def order(request):
    uid = request.session.get('user_id')
    cart = Cart.objects.filter(uid=uid, isselect=1)
    user = UserInfo.objects.filter(id=uid)
    address = UserAddress.objects.filter(user=uid)
    context = {'cart':cart, 'user':user, 'address':address[0]}
    return render(request, 'app_cart/place_order.html', context=context)


def order_handle(request):
    tran_id = transaction.savepoint()
    uid = request.session.get('user_id')
    cart = Cart.objects.filter(uid=uid, isselect=1)
    total = 0
    for one in cart:
        sub_total = one.gnumber * one.gid.gprice
        total += sub_total
    now = datetime.datetime.now
    # creat orderinfo
    try:
        order = OrderInfo()
        order.onumber = '%s%d'%(now().strftime('%Y%m%d%H%M%S'), uid)
        order.uid_id = uid
        order.ototal = total
        order.odate = now()
        order.oispay = False
        order.oaddress = ''
        order.save()

        #  creat detail order info
        for one in cart:
            detail = OrderDetailInfo()
            detail.oid = order
            detail.gid = one.gid
            detail.price = one.gid.gprice
            detail.count = one.gnumber
            detail.save()

        # deledt cart
        Cart.objects.filter(uid=uid, isselect=1).delete()
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        transaction.savepoint_rollback(tran_id)

    return JsonResponse({'hello':'hello'})


def pay(request):
    pass
