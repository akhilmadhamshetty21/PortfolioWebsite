from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('blogs', views.PostList.as_view(), name='blogs'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<str:cats>/', views.category, name='category')
]
