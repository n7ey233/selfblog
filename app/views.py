from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, JsonResponse
from .models import *
from .forms import *
import requests

def send_notification_telegram(text, bot_to_use=None):
    if bot_to_use == 'use_mebot':
        telegram_token = '761637360:AAHRihv6wse2Tf4cySR2G3mxxQft5buVGTU' #token telegi
        chat_id = '644654778'
    else:
        telegram_token = '700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg' #token telegi
        chat_id = '405347178'
    """id teleg
        http://n7ey233.pythonanywhere.com/automaximum_notif
        #moi id telegi '405347178'
        #id telegi antona '548383851'
        #id gruppi '-384637816'
        #chat_id = '405347178' #moy id v telege dlya otpravki
    """
    url = "https://api.telegram.org/bot"+telegram_token+"/sendMessage"
    data = {'chat_id': chat_id, 'text': text}
    requests.get(url,headers={'Content-Type': 'application/json' }, json=data)

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
        if object:form.fields["subcategory_of"].queryset = action.objects.all().exclude(pk=object.pk)
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
                return redirect('/?query='+request.GET.get('create'))
    else:           
        return render(request, 'app/form_page.html',{
        'form' : form,
        'page_title_prefix': page_title_prefix,
        'page_title': page_title,
        })
#action = request.GET.get('q').lower()
def automaximum_notif(request):
    """http://n7ey233.pythonanywhere.com/automaximum_notif
    """
    if request.GET.get('subject', '') == 'msg_landing_page_automaximum':
        text = "заявка на звонок: "+str(request.GET.get('query'))
        send_notification_telegram(text)
        return_dict = dict()
        return_dict['status'] = 'success'
        return_dict["len"] = 23
        return JsonResponse(return_dict)
    elif request.GET.get('subject', '') == 'vilki_line_test':
        #use_mebot - '786088675:AAHJl7-u6-PeujvDPw11OGYgkMMtdrJfBkc'
        #text - json
        text = request.GET.get('text', '')
        print(text)
        send_notification_telegram(text, 'use_mebot')
        return HttpResponse('')
    else:
        return None
#tut tol'ko otobrazhaem vse posti iz lichnogo dnevnika
# Create your views here.
"""
n7ey233
vlad911as123

0111naeb9896
"""
