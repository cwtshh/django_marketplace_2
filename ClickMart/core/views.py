from django.shortcuts import render, redirect
from django.contrib.auth import logout as logouts

# importa os modelos
from item.models import Category, Item

from .forms import SignUpForm


def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')
    categories = Category.objects.all()

    # passa os itens e categorias para o template
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories
    })

def contact(request):
    return render(request, 'core/contact.html')

def logout(request):
    if request.method == "POST":
        logouts(request)
        return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


