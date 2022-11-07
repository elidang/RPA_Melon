from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Top, Nation, Sea


def index(request):
    """
    TOP 100 목록 출력
    """
    page = request.GET.get('page', '1')

    chart_list = Top.objects.order_by('-likem')

    paginator = Paginator(chart_list, 10)
    page_obj = paginator.get_page(page)

    context = {'chart_list': page_obj}
    return render(request, 'chart/chart_top100_list.html', context)


def nation(request):
    """
    국내 목록 출력
    """
    page = request.GET.get('page', '1')

    chart_list = Nation.objects.order_by('-likem')

    paginator = Paginator(chart_list, 10)
    page_obj = paginator.get_page(page)

    context = {'chart_list': page_obj}
    return render(request, 'chart/chart_nation_list.html', context)


def sea(request):
    """
    국내 목록 출력
    """
    page = request.GET.get('page', '1')

    chart_list = Sea.objects.order_by('-likem')

    paginator = Paginator(chart_list, 10)
    page_obj = paginator.get_page(page)

    context = {'chart_list': page_obj}
    return render(request, 'chart/chart_sea_list.html', context)