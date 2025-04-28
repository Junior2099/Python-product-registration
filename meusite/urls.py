from django.contrib import admin
from django.urls import path
from minhaapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produto/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
    path('produto/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produto/remover/<int:produto_id>/', views.remover_produto, name='remover_produto'),
]
path('', views.home, name='home'),