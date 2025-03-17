from django.db import models

class Lease(models.Model):
    property_id = models.IntegerField()
    tenant_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Lease {self.id} - {self.tenant_name}"