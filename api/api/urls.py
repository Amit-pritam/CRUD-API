from django.urls import path,include
from api.views import ComapnyViewSet,EmployeeViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'companies',ComapnyViewSet)
router.register(r'employees',EmployeeViewSet)


urlpatterns = [

path('', include(router.urls))


]

