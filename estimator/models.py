from django.db import models
from estimator.utils.estimate import pcr


class Hospital(models.Model):
    """
    Model for hospital which includes all of the information
    to neatly present the hospital one the site, and encompassed
    by information required to find the price cost ratio
    """
    hospital_name = models.CharField(max_length=30)

    gross_revenue = models.IntegerField()
    contractual_adjustments = models.IntegerField()
    other_deductions = models.IntegerField()
    additions_to_revenue = models.IntegerField()

    deductions = models.IntegerField()
    net_revenue = models.IntegerField()
    price_cost_ratio = models.IntegerField()

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
        self.price_cost_ratio = pcr()
        super(Hospital, self).save(*args, **kwargs)