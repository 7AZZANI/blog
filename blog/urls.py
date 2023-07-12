from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.post_list, name= "listing"),
    path('post/<int:pk>/', views.post_details, name="post_detail"),
    path('post/new', views.post_form, name= "new_post"),
    path('post/<int:pk>/edit', views.post_edit, name= "post_edit"),
]