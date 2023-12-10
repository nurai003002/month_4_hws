from django.urls import path
from apps.settings.views import index1, index2, index3,index4

urlpatterns = [
    path('', index1, name='index1'),
    path('1', index2, name='index2'),
    path('2', index3, name='index3'),
    path('3', index4, name='index4')
]