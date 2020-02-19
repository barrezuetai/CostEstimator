from django.shortcuts import render


def home(request):
    return render(
        request,
        'estimator/base.html',
        {
            'title': 'Price Estimator',
        }
    )
