from django.shortcuts import render
from hello.models import User
# Create your views here.


def hello_random(req, name):
    # update the same record each time just to know who is the current user
    # save data
    user = User.objects.all()
    if user:
        user[0].name = name
        user[0].save()
    else:
        User(name=name).save()

    # pass data to the template
    ctx = {
        'name': name
    }
    return render(req, 'hello_index.html', ctx)
