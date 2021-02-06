from django.urls import path
from . import views
from .views import UserPostListView, PostDetailedView,PostDeleteView,PostCreateView

urlpatterns = [
    path('', views.home,name='app-home'),
    path('about/', views.about, name='app-about'),
    path('new/', PostCreateView.as_view(), name='add-task'),
    path('task/<str:username>/', UserPostListView.as_view(), name='user-task'),
    path('task/<str:username>/<int:pk>/', PostDetailedView.as_view(), name='detail-task'),
    path('task/<str:username>/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-task'),
]
