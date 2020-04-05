from django.shortcuts import render, redirect
from django.urls import reverse
from estimator.forms import HospitalForm
from django.views.generic import DetailView
from estimator.models import Hospital
from estimator.utils.estimate import generate_prices


class HospitalDetailView(DetailView):
    model = Hospital

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pcr = self.object.price_cost_ratio
        context['procedure_prices'] = generate_prices(pcr)
        return context


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
            if formset.instance.other_deductions is None:
                formset.instance.other_deductions = 0
            if formset.instance.contractual_adjustments is None:
                formset.instance.contractual_adjustments = 0
            if formset.instance.additions_to_revenue is None:
                formset.instance.additions_to_revenue = 0
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


def get_all_hospitals(request):
    all_hospitals = Hospital.objects.all()
    return render(
        request,
        "estimator/all.html",
        {"all_hospitals": all_hospitals}
    )
