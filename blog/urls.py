from django.urls import path
from . import views
urlpatterns = [
   path('', views.ListPostView.as_view(), name='blog'),
   path('<int:pk>/', views.post, name='post'),
]
