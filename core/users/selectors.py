from .models import User


def get_users_for_ids(user_ids):
    return User.objects.filter(id__in=user_ids)
