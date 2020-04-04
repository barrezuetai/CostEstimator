from django.forms import ModelForm, TextInput
from estimator.models import Hospital


class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = [
                    'hospital_name',
                    'gross_revenue',
                    'contractual_adjustments',
                    'other_deductions',
                    'additions_to_revenue'
                 ]

        widgets = {
            'hospital_name': TextInput(attrs={'placeholder': 'Hospital Name'}),
            'gross_revenue': TextInput(attrs={'placeholder': 'Gross Revenue'}),
            'contractual_adjustments': TextInput(
                attrs={'placeholder': 'Contractual Adjustments'}),
            'other_deductions': TextInput(
                attrs={'placeholder': 'Other Deductions'}),
            'additions_to_revenue': TextInput(
                attrs={'placeholder': 'Additions to Revenue'}),
        }

        labels = {
            'hospital_name': '',
            'gross_revenue': '',
            'contractual_adjustments': '',
            'other_deductions': '',
            'additions_to_revenue': ''
        }
