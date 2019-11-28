from django.shortcuts import render, HttpResponse

# Create your views here.
# 展示所有商品
goods_list = ['好丽友派', '雀巢咖啡', '口香糖', '辣条']


def all_goods(request):
    g_str = ''
    for g in goods_list:
        g_str += (g + '<br>')
    return HttpResponse(g_str)


# 添加商品
# def add_goods(request):
#     goods = request.GET.get('name')
#     if goods:
#         goods_list.append(goods)
#         return HttpResponse('添加成功')
#     else:
#         return HttpResponse('没有这个商品名称')

# 表单提交
def add_goods(request):
    if request.method == 'POST':
        goods = request.POST.get('gname')
        if goods:
            goods_list.append(goods)
            return HttpResponse('添加成功')
    else:
        return render(request, 'add_goods.html')


# 删除商品
def delete_goods(request):
    goods = request.GET.get('name')
    if goods in goods_list:
        goods_list.remove(goods)
        return HttpResponse('删除成功')
    else:
        return HttpResponse('不存在此商品名称！')


def update_goods(request, name):
    if request.method == 'POST':
        new_name = request.POST.get('gname')
        goods_list[2] = new_name
        return HttpResponse('更新成功')
    return render(request, 'update.html')
