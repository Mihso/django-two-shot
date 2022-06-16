from django.contrib import admin
from receipts.models import (
    Receipt, 
    ExpenseCategory, 
    Account,
    Money,
    )
# Register your models here.
class ReceiptAdmin(admin.ModelAdmin):
    pass

class ExpenseCategoryAdmin(admin.ModelAdmin):
    pass

class AccountAdmin(admin.ModelAdmin):
    pass

class MoneyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Money, MoneyAdmin)