from django.urls import path

from .views import (
    DownloadBouquets,
    SendCardsView,
    TokenCreateView,
    TokenDestroyView,
    ResellerListView,
    ResellerDetailView,
    ResellerEditView,
    ResellerDeleteView,
    ResellerActivateAPIView,
    ResellerRegisterAPIView,
    ResellerFilterCards,
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
    CardDelayedUpdatePackageView,
    CardDelayedRemovePackageView,
    CardForceUpdatePackageView,
    CardForceRemovePackageView,
    CardUpdateExpiredView,
    CardDeleteView,
    SubscriberListView,
    SubscriberDetailView,
    SubscriberEditView,
    SubscriberCreateView,
    SubscriberDeleteView,
    SubscriberUpdateCardsView,
    SubscriberUpdateBalanceView,
    SubscriberDeleteCardView,
    BouquetsFilterListView,
    SettingsView,
    ChangeSettingsView,
    SuspendSubscriptionView,
    CreateRangeCardView,
    TieCardsToResellerView,
    PickUpCardsFromReseller,
    ResellerTieOneCard,
    ResellerPickUpOneCard,
    MakeAdmin,
    ChangeSelfPermission,
    SynchronizeView,
    Dashboard,
    ReportSubsView,
    ReportCardsView,
    ReportLogsView,
    ReportFinanceView,
    ReportCardsOfResellerView,
    balance, BalanceUser)

app_name = 'main'

urlpatterns = [
    path('resellers/filter-cards/', ResellerFilterCards.as_view()),
    path('resellers/tie/cards/<int:pk>/', TieCardsToResellerView.as_view()),
    path('resellers/pickup/cards/<int:pk>/', PickUpCardsFromReseller.as_view()),
    path('resellers/tie/<int:pk>/', ResellerTieOneCard.as_view()),
    path('resellers/pickup/<int:pk>/', ResellerPickUpOneCard.as_view()),
    path('resellers/edit/<int:pk>/', ResellerEditView.as_view()),
    path('resellers/delete/<int:pk>/', ResellerDeleteView.as_view()),
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
    path('cards/delayed-add/package/<int:pk>/', CardDelayedUpdatePackageView.as_view()),
    path('cards/delayed-remove/package/<int:pk>/', CardDelayedRemovePackageView.as_view()),
    path('cards/edit/package/<int:pk>/', CardForceUpdatePackageView.as_view()),
    path('cards/edit/expired/<int:pk>/', CardUpdateExpiredView.as_view()),
    path('cards/edit/status/<int:pk>/', SuspendSubscriptionView.as_view()),
    path('cards/delete/package/<int:pk>/', CardForceRemovePackageView.as_view()),
    path('cards/delete/<int:pk>/', CardDeleteView.as_view()),
    path('cards/<int:pk>/', CardDetailView.as_view()),
    path('cards/create/range/', CreateRangeCardView.as_view()),
    path('cards/create/', CardCreateView.as_view()),
    path('cards/', CardListView.as_view()),
    path('subscribers/delete/<int:pk>/', SubscriberDeleteView.as_view()),
    path('subscribers/edit/balance/<int:pk>/', SubscriberUpdateBalanceView.as_view()),
    path('subscribers/edit/cards/<int:pk>/', SubscriberUpdateCardsView.as_view()),
    path('subscribers/edit/<int:pk>/', SubscriberEditView.as_view()),
    path('subscribers/delete/cards/<int:pk>/', SubscriberDeleteCardView.as_view()),
    path('subscribers/<int:pk>/', SubscriberDetailView.as_view()),
    path('subscribers/create/', SubscriberCreateView.as_view()),
    path('subscribers/', SubscriberListView.as_view()),
    path('password-reset/', ResetPasswordRequestView.as_view()),
    path('password/<str:sign>/',
         ResetPasswordView.as_view(),
         name='update_password'),
    path('download/<int:count>/', DownloadBouquets.as_view()),
    path('send/', SendCardsView.as_view()),
    path('bouquets/<int:pk>/', BouquetsFilterListView.as_view()),
    path('settings/', SettingsView.as_view()),
    path('change-settings/', ChangeSettingsView.as_view()),
    path('report-subs/', ReportSubsView.as_view()),
    path('report-card/', ReportCardsView.as_view()),
    path('report-logs/', ReportLogsView.as_view()),
    path('report-finance/', ReportFinanceView.as_view()),
    path('report-cards-reseller/', ReportCardsOfResellerView.as_view()),
    path('change-permission/<int:pk>/', MakeAdmin.as_view()),
    path('is-permission-editable/<int:pk>/', ChangeSelfPermission.as_view()),
    path('synchronize/', SynchronizeView.as_view()),
    path('dashboard/', Dashboard.as_view()),
    path('balance/', BalanceUser.as_view()),
]
