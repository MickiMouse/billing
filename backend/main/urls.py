from django.urls import path

from .views import SubscriberView, CardsView, ResellerActivateAPIView, ResellerRegisterAPIView

app_name = 'main'

urlpatterns = [
    path(
        'register_activate/<str:sign>/',
        ResellerActivateAPIView.as_view(),
        name='register_activate'
    ),
    path('register/reseller/', ResellerRegisterAPIView.as_view()),
    path('cards/<int:pk>/', CardsView.as_view()),
    path('subscribers/', SubscriberView.as_view()),
]
