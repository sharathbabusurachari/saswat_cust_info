from import_export import resources
from .models import (Report, CustomerDetails, WhatsAppCustomer, WhatsAppProspectInfo, WhatsAppLoanInfo,
                     WhatsAppInsuranceInfo)


class ReportResource(resources.ModelResource):
    class Meta:
        model = Report


class CustomerDetailsResource(resources.ModelResource):
    class Meta:
        model = CustomerDetails


class WhatsAppCustomerResource(resources.ModelResource):
    class Meta:
        model = WhatsAppCustomer


class WhatsAppProspectInfoResource(resources.ModelResource):
    class Meta:
        model = WhatsAppProspectInfo


class WhatsAppLoanInfoResource(resources.ModelResource):
    class Meta:
        model = WhatsAppLoanInfo


class WhatsAppInsuranceInfoResource(resources.ModelResource):
    class Meta:
        model = WhatsAppInsuranceInfo
