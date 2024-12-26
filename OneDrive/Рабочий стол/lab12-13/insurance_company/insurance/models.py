from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Policy(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='policies')
    policy_number = models.CharField(max_length=50)
    coverage_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.policy_number} - {self.client.name}"

class Claim(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='claims')
    claim_date = models.DateField()
    amount_claimed = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')])

    def __str__(self):
        return f"Claim for {self.policy.policy_number} - {self.status}"