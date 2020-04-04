from django.views.generic import DetailView
from estimator.models import Hospital


class HospitalDetailView(DetailView):
    model = Hospital


def home(request):
    return render(
        request,
        'estimator/base.html',
        {
            'title': 'Price Estimator',
        }
    )
