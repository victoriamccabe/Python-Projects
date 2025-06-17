from django.urls import path
from . import views

urlpatterns = [
    # Sets the url path to home page index.html
    path('', views.home, name='index'),
    # Sets the URL path to Create New Account page CreateNewAccount.html
    path('create/', views.create_account, name='create'),
    # Sets the URL path to Balance Sheet page BalanceSheet.html
    path('balance/', views.balance, name='balance'),
    # Sets the URL path to Add New Transaction page AddNewTransaction.html
    path('transaction/', views.transaction, name='transaction'),
    # Sets so the Balance Sheet can be displayed using a primary key
    path('<int:pk>/balance/', views.balance, name='balance'),
]