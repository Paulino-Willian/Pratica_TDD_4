from django.urls import path
from core.views import login, logout, home
from core.views_agenda import agenda_create, agenda_delete, agenda_list, agenda_update

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('index/', home, name='index'),
    path('', home, name='home'),

    # Agenda CRUD
    path('contatos/', agenda_list, name='agenda_list'),
    path('contatos/novo/', agenda_create, name='agenda_create'),
    path('contatos/<int:pk>/editar/', agenda_update, name='agenda_update'),
    path('contatos/<int:pk>/excluir/', agenda_delete, name='agenda_delete'),
]
