from django.shortcuts import render, HttpResponse, redirect
from .models import Stock
from .forms import StockCreateForm


# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World!')


def index(request):
    return render(request, 'index.html')


def show_stock(request):
    stock = Stock.objects.all()
    return render(request, 'show_stock.html', context={'stock': stock})


def add_stock(request):
    if request.method == 'POST':
        form = StockCreateForm(request.POST, request.FILES, category='Category1')
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'add_stock.html', context={'form': form})
    form = StockCreateForm(category='Category1')
    return render(request, 'add_stock.html', context={'form': form})


def delete_stock(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    if request.method == 'POST':
        stock.delete()
        return redirect('index')
    return render(request, 'confirm_delete_stock.html', context={'stock': stock})
