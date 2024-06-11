import random

from .models import Category


def categories(request):
    return {'categories': Category.objects.all()}


def random_categories(request):
    categories = list(Category.objects.all())
    random_categories = random.sample(categories, 8)
    return {'random_categories': random_categories}
