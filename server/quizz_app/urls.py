from rest_framework import routers
from .api import *
from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *
router = routers.DefaultRouter() 
router.register('questions', questionViewSet, 'questions' )

urlpatterns = [
    # url(r'^questions/$', QuestionView.as_view()),
    url(r'^profile/$', ProfileUpdateView.as_view()),
    url(r'^retrait/$', RetraitView.as_view()),
    url(r'^wallet/$', WalletView.as_view()),
]

urlpatterns += router.urls

