from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('create/', views.CreateUserViews.as_view(), name='create'),
    path('token/', views.CreateTokenViews.as_view(), name='token'),
    path('me/', views.ManageUserViews.as_view(), name='me'),
]
