import random

from .models import Category, Product


def categories(request):
    return {'categories': Category.objects.all()}


def random_product(request):
    try:
        product = list(Product.objects.all())
        random_product = random.sample(product, 8)
        first_part = random_product[:4]
        second_part = random_product[4:]
        return {'first_part': first_part, 'second_part': second_part}
    except Exception:
        return {'first_part': [], 'second_part': []}
