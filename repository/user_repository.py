user_repository = {}


def save(user):
    user_repository[user.id] = user


def get_by_id(user_id: str):
    return user_repository[user_id]
