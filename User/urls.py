from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserFormView,FormView
router = DefaultRouter()
router.register(r'',UserFormView)
urlpatterns = [
    path('',include(router.urls)),
    path('views', FormView.as_view()) #Other Method
    
]
