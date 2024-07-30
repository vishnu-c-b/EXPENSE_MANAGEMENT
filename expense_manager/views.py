from rest_framework import generics, views
from .models import Expense, ExpenseSplit
from .serializers import ExpenseSerializer
from django.db import models
from user_manager.models import User
import csv
from django.db.models import Sum
from django.http import HttpResponse

class ExpenseCreateView(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class UserExpensesView(generics.ListAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Expense.objects.filter(participants__id=user_id)

class OverallExpensesView(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class DownloadBalanceSheetView(views.APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="balance_sheet.csv"'

        writer = csv.writer(response)
        writer.writerow(['User', 'Total Amount', 'Individual Expenses'])

        # Fetch all users and their total expenses
        users = User.objects.all()
        overall_total = 0

        for user in users:
            total_amount = ExpenseSplit.objects.filter(user=user).aggregate(total=Sum('amount'))['total'] or 0
            overall_total += total_amount
            # Write the total amount row
            writer.writerow([user.email, f'{total_amount:.2f}'])

            # Fetch individual expenses for the user
            individual_expenses = ExpenseSplit.objects.filter(user=user)
            for expense in individual_expenses:
                amount = expense.amount or 0
                writer.writerow(['', '', f'{amount:.2f}'])

        # Write overall total expenses for all users at the end
        writer.writerow([])
        writer.writerow(['Overall Total', f'{overall_total:.2f}'])

        return response