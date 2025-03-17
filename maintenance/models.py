from django.db import models

class MaintenanceRequest(models.Model):
    lease_id = models.IntegerField()  # Link to a lease
    description = models.TextField()
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ])

    def __str__(self):
        return f"Request {self.id} - Lease {self.lease_id} - {self.status}"