from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME",
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

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': "Some text",
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

    return render(request, 'main/about.html', context)