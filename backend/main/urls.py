from django.urls import path

from .views import (
    DownloadBouquets,
    TokenCreateView,
    TokenDestroyView,
    ResellerListView,
    ResellerDetailView,
    ResellerActivateAPIView,
    ResellerRegisterAPIView,
    ResetPasswordRequestView,
    ResetPasswordView,
    PackageListView,
    PackageFilterListView,
    PackageDetailView,
    PackageCreateView,
    PackageDeleteView,
    PackageEditView,
    PackageUpdateBouquetsView,
    PackageRemoveBouquetsView,
    CardListView,
    CardDetailView,
    CardCreateView,
    CardUpdateStatusView,
    CardUpdatePackageView,
    CardRemovePackageView,
    CardUpdateExpiredView,
    SubscriberListView,
    SubscriberDetailView,
    SubscriberCreateView,
    SubscriberDeleteView,
    SubscriberUpdateCardsView,
    SubscriberUpdateBalanceView,
    SubscriberDeleteCardView,
    BouquetsFilterListView,
    SettingsView,
    ChangeSettingsView,
)

app_name = 'main'

urlpatterns = [
    path('resellers/<int:pk>/', ResellerDetailView.as_view()),
    path('resellers/', ResellerListView.as_view()),
    path('register/reseller/', ResellerRegisterAPIView.as_view()),
    path('register_activate/<str:sign>/',
         ResellerActivateAPIView.as_view(),
         name='register_activate'),
    path('token/login/', TokenCreateView.as_view()),
    path('token/logout/', TokenDestroyView.as_view()),
    path('packages-filter/<int:pk>/', PackageFilterListView.as_view()),
    path('packages/delete/<int:pk>/', PackageDeleteView.as_view()),
    path('packages/edit/bouquets/<int:pk>/', PackageUpdateBouquetsView.as_view()),
    path('packages/delete/bouquets/<int:pk>/', PackageRemoveBouquetsView.as_view()),
    path('packages/edit/tariff/<int:pk>/', PackageEditView.as_view()),
    path('packages/<int:pk>/', PackageDetailView.as_view()),
    path('packages/create/', PackageCreateView.as_view()),
    path('packages/', PackageListView.as_view()),
    path('cards/edit/status/<int:pk>/', CardUpdateStatusView.as_view()),
    path('cards/edit/package/<int:pk>/', CardUpdatePackageView.as_view()),
    path('cards/edit/expired/<int:pk>/', CardUpdateExpiredView.as_view()),
    path('cards/delete/package/<int:pk>/', CardRemovePackageView.as_view()),
    path('cards/<int:pk>/', CardDetailView.as_view()),
    path('cards/create/', CardCreateView.as_view()),
    path('cards/', CardListView.as_view()),
    path('subscribers/delete/<int:pk>/', SubscriberDeleteView.as_view()),
    path('subscribers/edit/balance/<int:pk>/', SubscriberUpdateBalanceView.as_view()),
    path('subscribers/edit/cards/<int:pk>/', SubscriberUpdateCardsView.as_view()),
    path('subscribers/delete/cards/<int:pk>/', SubscriberDeleteCardView.as_view()),
    path('subscribers/<int:pk>/', SubscriberDetailView.as_view()),
    path('subscribers/create/', SubscriberCreateView.as_view()),
    path('subscribers/', SubscriberListView.as_view()),
    path('password-reset/', ResetPasswordRequestView.as_view()),
    path('password/<str:sign>/',
         ResetPasswordView.as_view(),
         name='update_password'),
    path('download/<int:count>/', DownloadBouquets.as_view()),
    path('bouquets/<int:pk>/', BouquetsFilterListView.as_view()),
    path('settings/', SettingsView.as_view()),
    path('change-settings/', ChangeSettingsView.as_view()),
]
