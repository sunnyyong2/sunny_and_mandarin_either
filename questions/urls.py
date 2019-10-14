from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:q_id>/', views.detail, name='detail'),
    path('<int:q_id>/update/', views.update, name='update'),
    path('<int:q_id>/delete/', views.delete, name='delete'),
    path('<int:q_id>/<int:c_id>/', views.choice_update, name="choice_update"),
    path('<int:q_id>/<int:c_id>/comment',
         views.create_comment, name='create_comment'),

]
