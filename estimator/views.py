from django.shortcuts import render, redirect
from django.urls import reverse
from estimator.forms import HospitalForm
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


def create_hospital_page(request):
    if request.method == 'POST':
        formset = HospitalForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            id = formset.instance.id
            return redirect(reverse("hospital_detail", args=(id,)))
    else:
        formset = HospitalForm()
    return render(
        request,
        'estimator/manage_hospital.html',
        {'formset': formset}
    )


