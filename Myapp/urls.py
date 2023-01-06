from xml.etree.ElementInclude import include

from django.urls import path
from Myapp import views, Api
urlpatterns = [
    path('',views.home,name='home'),
    path('data', views.dht11, name='Data'),
    path('chart', views.chart, name='chart'),
    path('archive', views.archive, name='archive'),
    path('history24', views.history24, name='history24'),
    path('export_xls24h', views.export_xls24h, name = 'export_xls24h'),
    path('export_xls48h', views.export_xls48h, name='export_xls48h'),
    path('export_xlsweek', views.export_xlsweek, name='export_xlsweek'),
    path('graph_24h', views.graph_24h, name='graph_24h'),
    path('table',views.table,name='table'),


##Api
    path('api/list', Api.Dlist, name ='DHT11List'),
    path('api/post', Api.Dhtviews.as_view(), name ='DHT_post'),

]


