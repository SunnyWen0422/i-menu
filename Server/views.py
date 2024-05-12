import json
import random
from .models import Dish
from django.http import HttpResponse
from .forms import MenuForm
from django.shortcuts import render
import mysql.connector  # 导入mysql的连接器
# 连接到MySQL数据库
def connect_to_mysql():
    conn = mysql.connector.connect(
        host='127.0.0.1',  # 例如: localhost
        user='root',  # 你的数据库用户名
        password='770609',  # 你的数据库密码
        database='menu'  # 你的数据库名
    )
    return conn

def get_menu(request):
    if request.method == 'GET':
        return render(request, 'runserver.html', {})


def result(request):
    if request.method == 'GET':
        all_dishes = Dish.objects.all()    # 获取所有菜品
        form = MenuForm(request.GET)
        if form.is_valid():
            meat_count = form.cleaned_data['meat_count']
            veggie_count = form.cleaned_data['veggie_count']

    # 根据类型筛选菜品并随机选择
    meat_dishes = []
    veggie_dishes = []
    for dish in all_dishes:
        if dish.type == 1:  # 如果菜品类型为meat，则添加到meat列表中
            meat_dishes.append(dish)
        elif dish.type == 2:  # 如果菜品类型为veggie，则添加到veggie列表中
            veggie_dishes.append(dish)

            # 根据用户的选择筛选出指定数量的荤菜和素菜
    selected_meat_dishes = random.sample(meat_dishes, min(int(meat_count), len(meat_dishes)))
    selected_veggie_dishes = random.sample(veggie_dishes, min(int(veggie_count), len(veggie_dishes)))

    context = {
        'selected_meat_dishes': selected_meat_dishes,
        'selected_veggie_dishes': selected_veggie_dishes,
    }
    return render(request, 'result.html', {'meat_dishes': selected_meat_dishes, 'veggie_dishes': selected_veggie_dishes})