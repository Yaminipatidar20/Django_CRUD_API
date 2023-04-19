from django.urls import path
from .views import *

urlpatterns = [
    path('GetEd/', GetEd.as_view()),
    path('PostEd/', PostEd.as_view()),
    path('PutEd/', PutEd.as_view()),
    path('PatchtEd/', PatchtEd.as_view()),
    path('DeleteEd/<int:pk>', DeleteEd.as_view()),
]
