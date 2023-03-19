from hello.models import User


def user(req):
    user = User.objects.all()[0]
    return {
        'user': user
    }
