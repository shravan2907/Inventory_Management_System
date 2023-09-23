from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Transactions
from .forms import ProductForm, TransactionForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.



@login_required
def index(request):
    transactions = Transactions.objects.all()
    products = Product.objects.all()
    workers_count = User.objects.all().count()
    transactions_count = Transactions.objects.all().count()
    items_count = Product.objects.all().count()
    if request.method == 'POST':
         form = TransactionForm(request.POST)
         if form.is_valid():
              instance = form.save(commit=False)
              instance.staff = request.user
              instance.save()
              return redirect('dashboard-index')
    else:
         form = TransactionForm()
    context = {
         'transactions':transactions,
         'form':form,
         'products':products,
         'workers_count':workers_count,
         'transactions_count':transactions_count,
         'items_count':items_count
    }
    return render(request,'dashboard/index.html',context)


##########################################################################
@login_required
def staff(request):
     workers = User.objects.all()
     workers_count = workers.count()
     transactions_count = Transactions.objects.all().count()
     items_count = Product.objects.all().count()
     context = {
          'workers':workers,
          'workers_count':workers_count,
          'transactions_count':transactions_count,
          'items_count':items_count
     }
     return render(request,'dashboard/staff.html', context)
######################################################################################
@login_required
def staff_detail(request, pk):
     workers = User.objects.get(id=pk)
     context = {
          'workers':workers,
          
     }
     return render(request, 'dashboard/staff_detail.html', context)
############################################################################
@login_required
def products(request):
     items = Product.objects.all()
     transactions = Transactions.objects.all()
     items_count = items.count()
     #items = Product.objects.raw('SELECT * FROM dashboard_product')
     workers_count = User.objects.all().count()
     transactions_count = Transactions.objects.all().count()
     if request.method == 'POST':
          form = ProductForm(request.POST)
          if form.is_valid():
               form.save()
               product_name = form.cleaned_data.get('name')
               messages.success(request, f'{product_name} has been added')
               return redirect('dashboard-products')
     else:
          form = ProductForm()
     context = {
          'items':items,
          'form':form,
          'workers_count':workers_count,
          'transactions_count':transactions_count,
          'items_count':items_count
     }
     return render(request, 'dashboard/products.html',context)
###########################################################################################
@login_required
def products_delete(request, pk):
     item  = Product.objects.get(id=pk)
     if request.method=='POST':
          item.delete()
          return redirect('dashboard-products')
     return render(request, 'dashboard/product_delete.html')
#################################################################################
@login_required
def products_update(request, pk):
     item = Product.objects.get(id=pk)
     if request.method=='POST':
          form = ProductForm(request.POST, instance=item)
          if form.is_valid():
               form.save()
               return redirect('dashboard-products')
     else:
          form = ProductForm(instance=item)

     context = {
          'form':form
          
     }
     return render(request, 'dashboard/product_update.html', context)

##############################################################
@login_required
def transactions(request):
     transaction = Transactions.objects.all()
     transactions_count = transaction.count()
     workers_count = User.objects.all().count()
     items_count = Product.objects.all().count()

     context = {
          'transactions':transaction,
          'workers_count':workers_count,
          'transactions_count':transactions_count,
          'items_count':items_count
     }
     return render(request, 'dashboard/transactions.html',context)