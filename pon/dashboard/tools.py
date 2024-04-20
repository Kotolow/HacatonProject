from db_app.models import User
from pon.consts import POSSIBLE_TAGS


def recomendations(request):
    if request.user.is_authenticated:
        POSSIBLE_TAGS = User.tags.split(',')
    return POSSIBLE_TAGS
