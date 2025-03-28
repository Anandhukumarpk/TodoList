
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app import views


router = routers.SimpleRouter()
router.register('todo',views.TodoViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls))
]
