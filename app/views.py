from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import *
from .forms import *


def main(request):
    #post_list = post.objects.all().order_by('-created_date')
    page = 'main'
    page_name = 'Главная'
    obj_list = None
    button_name = None
    zapros = request.GET.get('query', '')
    if zapros != '': 
        page = zapros
        if page == 'action': 
            page_name = "Действия"
            button_name = 'Новое действие'
            obj_list = action.objects.all()
        elif page == 'purchase':
            page_name = 'Покупки'            
            button_name = 'Новая покупка'
            obj_list = purchase.objects.all()
        elif page == 'knowledge':
            page_name = 'Знания'
            button_name = 'Новое знание'
            obj_list = knowledge.objects.all()
        elif page == 'tracking_number':
            page_name = '快递单号码'
            button_name = '创造新快递单号码'
            obj_list = tracking_number.objects.all()
        else:
            page = 'main'
        try:
            if len(obj_list) == 0:obj_list = None
        except: None
        #page = 
    return render(request, 'app/main.html',{
        'nav_bar': 'blog',
        'page_name': page_name,
        'obj_list': obj_list,
        'button_name': button_name,
        'page': page,
        })


def form_page(request):
    form = None
    object = None
    page_title = None
    redirecting_page = None
    if request.GET.get('id', '') != '':page_title_prefix = 'Редактирование'
    else:page_title_prefix = 'Создание'
    if request.GET.get('create') == 'action':
        if request.GET.get('id', '') != '':
            object = action.objects.get(pk=request.GET.get('id'))
        page_title = 'Действие'
        form = actionForm(instance=object)
    elif request.GET.get('create') == 'purchase':
        if request.GET.get('id', '') != '':
            object = purchase.objects.get(pk=request.GET.get('id'))
        page_title = 'Покупка'
        form = purchaseForm(instance=object)
    elif request.GET.get('create') == 'knowledge':
        if request.GET.get('id', '') != '':
            object = knowledge.objects.get(pk=request.GET.get('id'))
        page_title = 'Знание'
        form = knowledgeForm(instance=object)
    elif request.GET.get('create') == 'tracking_number':
        if request.GET.get('id', '') != '':
            object = tracking_number.objects.get(pk=request.GET.get('id'))
        page_title = 'Номер отслеживания'
        form = tracking_numberForm(instance=object)
    if request.method == "POST":
        if request.POST.get('deleteit') == 'true':
            object.delete()
            return redirect('main')
        if request.GET.get('create') == 'action':
            form = actionForm(request.POST, instance=object)
            redirecting_page = '/'
        elif request.GET.get('create') == 'purchase':
            form = purchaseForm(request.POST, instance=object)
            redirecting_page = '/about_me'
        elif request.GET.get('create') == 'knowledge':
            form = knowledgeForm(request.POST, instance=object)
            redirecting_page = '/about_me'
        elif request.GET.get('create') == 'tracking_number':
            form = tracking_numberForm(request.POST, instance=object)
            redirecting_page = '/about_me'
        if form.is_valid():
            i = form.save()
            i.save()
            if request.POST.get('continute') == 'true':
                return redirect('/form_page?create='+request.GET.get('create')+'&id=%s' % (i.pk))
            elif request.POST.get('add_new') == 'true':
                return redirect('/form_page?create='+request.GET.get('create'))
            else:
                return redirect('/query='+request.GET.get('create'))
    else:           
        return render(request, 'app/form_page.html',{
        'form' : form,
        'page_title_prefix': page_title_prefix,
        'page_title': page_title,
        })
#action = request.GET.get('q').lower()
#tut tol'ko otobrazhaem vse posti iz lichnogo dnevnika
# Create your views here.

