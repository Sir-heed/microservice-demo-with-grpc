import random
from .models import User

def get_random_user():
    users = User.objects.all()
    while users.count() == 0:
        User.objects.create()
        users = User.objects.all()
    return random.choice(users)