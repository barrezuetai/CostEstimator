from django.db import models
from estimator.utils.estimate import get_pcr as pcr


class Hospital(models.Model):
    """
    Model for hospital which includes all of the information
    to neatly present the hospital one the site, and encompassed
    by information required to find the price cost ratio
    """
    hospital_name = models.CharField(max_length=30)

    gross_revenue = models.IntegerField()
    contractual_adjustments = models.IntegerField(blank=True, null=True)
    other_deductions = models.IntegerField(blank=True, null=True)
    additions_to_revenue = models.IntegerField(blank=True, null=True)

    deductions = models.IntegerField()
    net_revenue = models.IntegerField()
    price_cost_ratio = models.DecimalField(max_digits=10, decimal_places=9)

    def save(self, *args, **kwargs):
        """
        Overriding save function in order to
        make calculations from the collected data
        before information is saved into the database
        """
        self.deductions = (self.contractual_adjustments
                           + self.other_deductions)
        self.net_revenue = (self.gross_revenue
                            + self.additions_to_revenue
                            - self.deductions)
        hospital_finances = {}
        hospital_finances['net_revenue'] = self.net_revenue
        hospital_finances['gross_revenue'] = self.gross_revenue
        self.price_cost_ratio = pcr(hospital_finances)
        print(self.price_cost_ratio)
        super(Hospital, self).save(*args, **kwargs)
