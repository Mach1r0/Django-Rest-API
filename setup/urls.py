from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]