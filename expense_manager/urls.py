# expenses/urls.py
from django.urls import path
from .views import ExpenseCreateView, UserExpensesView, OverallExpensesView, DownloadBalanceSheetView

urlpatterns = [
    path('create/', ExpenseCreateView.as_view(), name='create-expense'),
    path('user/<int:user_id>/', UserExpensesView.as_view(), name='user-expenses'),
    path('overall/', OverallExpensesView.as_view(), name='overall-expenses'),
    path('download-balance-sheet/', DownloadBalanceSheetView.as_view(), name='download-balance-sheet'),
]
