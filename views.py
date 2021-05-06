from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from deposit.models import Deposit


def index(request):

    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )


def add_user(request):

    if request.method == 'POST':

        deposit = deposit(
            deposit=request.POST['name'],
            term=request.POST['integer'],
            rate=request.POST['float']
        )

        deposit.save()

        context = {

        }

        return render(
            template_name='deposit_detail.html',
            request=request,
            context=context,

        )

    return render(
        template_name='deposit_detail',
        request=request
    )


def get_user(request, user_id):

    deposit = deposit.objects.get(pk=user_id)

    context = {

    }

    return render(
        template_name='user.html',
        request=request,
        context=context,

    )
