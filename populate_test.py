import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
import django
django.setup()

from your_app.models import Category, Item


def populate():
    # create some sample items
    tshirts = [
        {'title': 'Vintage Nirvana T-Shirt',
         'description': 'Size M, black, 100% cotton',
         'price': 20.0,
         'condition': 'Used',
         'image': 'nirvana_tshirt.jpg'},
        {'title': 'Retro 80s Rainbow T-Shirt',
         'description': 'Size S, white, 50% cotton/50% polyester',
         'price': 15.0,
         'condition': 'Used',
         'image': 'rainbow_tshirt.jpg'},
        {'title': 'Classic Plain White Tee',
         'description': 'Size L, white, 100% cotton',
         'price': 10.0,
         'condition': 'New',
         'image': 'plain_white_tshirt.jpg'}
    ]

    pants = [
        {'title': 'Levi\'s 501 Jeans',
         'description': 'Size 32x32, blue, 100% cotton',
         'price': 50.0,
         'condition': 'Used',
         'image': 'levis_501.jpg'},
        {'title': 'Adidas Track Pants',
         'description': 'Size M, black, 80% cotton/20% polyester',
         'price': 30.0,
         'condition': 'New with tags',
         'image': 'adidas_track_pants.jpg'}
    ]

    shoes = [
        {'title': 'Converse Chuck Taylor All Star',
         'description': 'Size 9, white, canvas',
         'price': 40.0,
         'condition': 'Used',
         'image': 'converse_all_star.jpg'},
        {'title': 'Nike Air Force 1',
         'description': 'Size 10, black, leather',
         'price': 80.0,
         'condition': 'Used',
         'image': 'nike_air_force_1.jpg'}
    ]

    # create categories and add items to them
    categories = {
        'T-Shirts': {'items': tshirts},
        'Pants': {'items': pants},
        'Shoes': {'items': shoes},
    }

    for category_name, category_data in categories.items():
        category = add_category(category_name)
        for item_data in category_data['items']:
            add_item(category, **item_data)


def add_item(category, title, description, price, condition, image):
    item = Item.objects.get_or_create(category=category, title=title, description=description, price=price, condition=condition)[0]
    item.image = image
    item.save()
    return item


def add_category(name):
    category = Category.objects.get_or_create(name=name)[0]
    return category


if __name__ == '__main__':
    print('Starting population script...')
    populate()
