from django.urls import path
from .views import SignupView, AccountEditView, AccountDeleteView, AccountDetailView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('edit_account/', AccountEditView.as_view(), name='account_edit'),
    path('delete_account/', AccountDeleteView.as_view(), name='account_delete'),

    path('account/<int:pk>/', AccountDetailView.as_view(), name='account_detail')
]