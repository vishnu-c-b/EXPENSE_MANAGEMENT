
from rest_framework import serializers
from .models import Expense, ExpenseSplit
from user_manager.serializers import User


class ExpenseSplitSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = ExpenseSplit
        fields = ['user', 'amount', 'percentage']


class ExpenseSerializer(serializers.ModelSerializer):
    paid_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    splits = ExpenseSplitSerializer(many=True, source='expensesplit_set')

    class Meta:
        model = Expense
        fields = ['description', 'amount', 'paid_by', 'split_method', 'splits', 'created_at']

    def validate(self, data):
        splits_data = data['expensesplit_set']
        if data['split_method'] == 'percentage':
            total_percentage = sum([split['percentage'] for split in splits_data])
            if total_percentage != 100:
                raise serializers.ValidationError("Percentages must add up to 100%")
        elif data['split_method'] == 'exact':
            total_amount = sum([split['amount'] for split in splits_data])
            if total_amount != data['amount']:
                raise serializers.ValidationError("Exact amounts must add up to the total amount")
        return data

    def create(self, validated_data):
        splits_data = validated_data.pop('expensesplit_set')
        expense = Expense.objects.create(**validated_data)
        if expense.split_method == 'equal':
            equal_amount = validated_data['amount'] / len(splits_data)
            for split_data in splits_data:
                ExpenseSplit.objects.create(
                    expense=expense, 
                    user=split_data['user'], 
                    amount=equal_amount, 
                    percentage=(equal_amount / validated_data['amount']) * 100
                )
        elif expense.split_method == 'percentage':
            for split_data in splits_data:
                percentage = split_data['percentage']
                amount = (percentage / 100) * validated_data['amount']
                ExpenseSplit.objects.create(
                    expense=expense, 
                    user=split_data['user'], 
                    amount=amount, 
                    percentage=percentage
                )
        elif expense.split_method == 'exact':
            total_amount = validated_data['amount']
            for split_data in splits_data:
                amount = split_data['amount']
                percentage = (amount / total_amount) * 100
                ExpenseSplit.objects.create(
                    expense=expense, 
                    user=split_data['user'], 
                    amount=amount, 
                    percentage=percentage
                )
        return expense
