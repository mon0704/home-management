from django.db import models

class Payment(models.Model):
    lease_id = models.IntegerField()  # Link to a lease
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('overdue', 'Overdue')
    ])

    def __str__(self):
        return f"Payment {self.id} - Lease {self.lease_id} - {self.amount}"