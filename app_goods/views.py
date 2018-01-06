from django.shortcuts import render
from .models import *
from app_user.models import BrowseHistory, UserInfo
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    # GoodsInfo.objects.filter(ttype=1).order[0:4]

    typelist = TypeInfo.objects.all()
    type10 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type20 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    context = {
        'type10':type10,
        'type11':type11,
        'type20':type20,
        'type21':type21,
    }
    return render(request, 'app_goods/index.html', context=context)

def detail(request,gid):
    goods = GoodsInfo.objects.get(id=gid)
    goods.gclick = goods.gclick + 1
    goods.save()
    if request.session.has_key('user_id'):
        uid = request.session.get('user_id')
        one_history = BrowseHistory()
        one_history.uid = UserInfo.objects.get(id=uid)
        one_history.gid = goods
        one_history.save()

    adv = GoodsInfo.objects.order_by('-id')[0:2]

    context = {'goods':goods,
               'adv1':adv[0],
               'adv2':adv[1],
               }
    return render(request, 'app_goods/detail.html', context=context)

def list(request, tid):
    page_number = request.GET.get('page',1)
    print('**********',page_number)
    tid = int(tid)
    type = TypeInfo.objects.get(id=tid)
    goods = type.goodsinfo_set.all()
    news = GoodsInfo.objects.order_by('-id')[0:2]

    paginator = Paginator(goods, 2)
    page = paginator.page(page_number)

    context = {'news':news, 'paginator':paginator, 'page':page}
    return render(request,'app_goods/list.html', context=context)

from haystack.views import SearchView

# class MySearch(SearchView):
#     def extra_context(self):