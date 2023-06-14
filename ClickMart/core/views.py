from django.shortcuts import render

# importa os modelos
from item.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    # passa os itens e categorias para o template
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories
    })

def contact(request):
    return render(request, 'core/contact.html')
