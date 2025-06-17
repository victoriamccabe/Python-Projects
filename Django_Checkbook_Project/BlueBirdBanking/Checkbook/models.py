from django.db import models
from datetime import date

# Creates the Account Model
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(decimal_places=2, max_digits=15)

    # Defines the model Manager for Accounts
    Accounts = models.Manager()

    # Allows references to a specific account be returned as the owner's name not the primary key
    def __str__(self):
        return self.first_name + " " + self.last_name[0]

# Choices for a transaction
TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]

# Creates the Transaction Model
class Transaction(models.Model):
    date = models.DateField(default=date.today)
    type = models.CharField(choices=TransactionTypes, max_length=10)
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # Defines the model Manager for Transaction
    Transactions = models.Manager()