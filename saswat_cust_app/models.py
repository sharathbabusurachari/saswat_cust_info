from django.db import models
import uuid

# Create your models here.


class Report(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class CustomerDetails(models.Model):
    YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]

    vle_name = models.CharField(max_length=50)
    customer_name_on_pan = models.CharField(max_length=50)
    father_name_or_spouse_name = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    address_on_aadhar = models.CharField(max_length=50)
    is_mobile_no_linked_to_aadhar = models.BooleanField(max_length=20, choices=YES_NO_CHOICES, default=True)

    def __str__(self):
        return self.customer_name_on_pan


class WhatsAppCustomer(models.Model):
    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('YES', 'No'),
    ]
    uuid = models.UUIDField(default=uuid.UUID('550e8400-e29b-41d4-a716-446655440000'), editable=False)
    customer_id = models.IntegerField(primary_key=True,)
    customer_id_version = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    relationship_manager = models.CharField(max_length=50)
    relationship_manager_mobile_no = models.IntegerField()
    customer_onboarded = models.CharField(max_length=3, choices=YES_NO_CHOICES, default=True)
    cluster_name = models.CharField(max_length=50)
    state_name = models.CharField(max_length=50)
    mother_tongue = models.CharField(max_length=50)
    bridge_language = models.CharField(max_length=50)
    customer_name_in_mothertongue = models.CharField(max_length=50)
    calling_name_in_mothertongue = models.CharField(max_length=50)
    calling_name_in_english = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name


class WhatsAppProspectInfo(models.Model):
    uuid = models.IntegerField()
    customer_id = models.ForeignKey(WhatsAppCustomer, on_delete=models.CASCADE)
    prospect_id = models.IntegerField(primary_key=True)
    loan_no_NBFC = models.CharField(max_length=50)
    loan_from = models.CharField(max_length=50)
    loan_amt = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.loan_no_NBFC


class WhatsAppLoanInfo(models.Model):
    uuid_loan = models.IntegerField()
    customer_id = models.ForeignKey(WhatsAppCustomer, on_delete=models.CASCADE)
    prospect_id = models.ForeignKey(WhatsAppProspectInfo, on_delete=models.CASCADE)
    saswat_loan_number = models.IntegerField()
    loan_no_NBFC = models.CharField(max_length=50)
    loan_from = models.CharField(max_length=50)
    loan_amt = models.DecimalField(max_digits=10, decimal_places=2)
    emi_amt = models.DecimalField(max_digits=10, decimal_places=2)
    emi_date = models.DateField()
    balance_loan_amt = models.DecimalField(max_digits=10, decimal_places=2)
    loan_type = models.CharField(max_length=50)
    loan_status_active = models.BooleanField(default=True)
    total_no_installment = models.IntegerField()
    no_installment_paid = models.IntegerField()
    overdue_installment = models.IntegerField()
    overdue_amt = models.DecimalField(max_digits=10, decimal_places=2)
    penalty_fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.loan_from


class WhatsAppInsuranceInfo(models.Model):
    uuid_insurance = models.IntegerField()
    customer_id = models.ForeignKey(WhatsAppCustomer, on_delete=models.CASCADE)
    policy_no_of_Insurance = models.CharField(max_length=50)
    saswat_loan_number = models.IntegerField()
    loan_from = models.CharField(max_length=50)
    Insurance_from = models.CharField(max_length=50)
    insured_amount = models.DecimalField(max_digits=10, decimal_places=2)
    No_of_cattle = models.IntegerField()
    insured_date = models.DateField()
    insurance_validity_date = models.DateField()
    Insurance_type = models.CharField(max_length=100)
    insurance_status_active = models.BooleanField(default=True)

    def __str__(self):
        return self.policy_no_of_Insurance


class WhatsAppOnBoarding(models.Model):
    mobile_no = models.CharField(max_length=15)
    status = models.CharField(max_length=8)
    Language_selected = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=10, help_text="Enter your postal code")
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)

    def __str__(self):
        return self.state
