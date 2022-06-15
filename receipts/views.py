from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from receipts.models import Receipt, Account, ExpenseCategory
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = ("receipts/list.html")
    def get_queryset(self):
        return Receipt.objects.filter(purchaser=self.request.user)

class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    template_name = ("receipts/create.html")
    fields = ["vendor", "total", "tax", "date", "category", "account"]
    def form_valid(self, form):
        item = form.save(commit=False)
        item.purchaser = self.request.user
        item.save()
        return redirect("home")

class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = ("accounts/list.html")
    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)

class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = ("accounts/create.html")
    fields = ["name", "number"]
    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("account")

class ExpenseCategoryListView(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    template_name = ("e_categories/list.html")
    def get_queryset(self):
        return ExpenseCategory.objects.filter(owner=self.request.user)

class ExpenseCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ExpenseCategory
    template_name = ("e_categories/create.html")
    fields = ["name"]
    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("list_categories")
