from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    #main^ main\about
    url(r'^$', views.main, name='main'),
    url(r'^form_page$', views.form_page, name='form_page'),
    url(r'^automaximum_notif$', views.automaximum_notif, name='automaximum_notif'),
    #sozdaniye abonenta
    #url(r'^abonent/create$', views.abonent_create, name='abonent_create'),
    #prosmotr
    #url(r'^abonent/view$', views.abonent_view, name='abonent_view'),
    #redaktirovaniye
    #url(r'^abonent/edit$', views.abonent_edit, name='abonent_edit'),
    #poisk abonenta
    #url(r'^abonent/search$', views.abonent_search, name='abonent_search'),

    #dobavleniye remarki
    #url(r'^add_remark$', views.add_remark, name='add_remark'),
    #dobavleniye excel fila
    #url(r'^add_excel$', views.add_excel, name='add_excel'),
    #url(r'^receive_data$', views.receive_data, name='receive_data'),
]