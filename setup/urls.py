from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
routers.register('cursos', CursosViewSet, basename='Cursos')
routers.register('alunos', AlunosViewSet, basename='Alunos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
