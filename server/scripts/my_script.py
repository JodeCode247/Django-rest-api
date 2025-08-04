# from server.models import Book


# book_obj,created=Book.objects.get_or_create(author="john",title='Everything between')

# if created:
#     print('done')

# scripts/my_script.py
def run(*args):
    print("This script is running via django-extensions!")
    # Access Django models or settings as needed