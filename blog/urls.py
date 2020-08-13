

from django.urls import path
from . import views


#from boletin import views
#from boletin.views inicio
app_name='blog'
urlpatterns = [

    path('',views.all_blogs,name='all_blogs'),
    path('<int:blog_id>/',views.detail,name='detail'),

    #url(r'^contact/$', views.contact, name='contact'),
    #url(r'^$', views.inicio, name='inicio'),
]
