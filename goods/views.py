from django.shortcuts import render

context = {
    'catalog': [
        'Все товары',
        'Кухня',
        'Спальня',
        'Гостинная',
        'Офис',
        'Фурнитура',
        'Декор',
    ]
}

def catalog(request):
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html', context)
