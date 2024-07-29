from django.db import models
from user_manager.models import User

class Expense(models.Model):
    SPLIT_METHODS = (
        ('equal', 'Equal'),
        ('exact', 'Exact'),
        ('percentage', 'Percentage'),
    )

    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_by = models.ForeignKey(User, related_name='expenses_paid', on_delete=models.CASCADE)
    split_method = models.CharField(max_length=10, choices=SPLIT_METHODS)
    participants = models.ManyToManyField(User, through='ExpenseSplit')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.description} - {self.amount}'
    
class ExpenseSplit(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f'{self.expense} - {self.user}'