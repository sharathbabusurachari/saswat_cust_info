from django.contrib import admin
from saswat_cust_app.models import (CustomerDetails, WhatsAppCustomer, WhatsAppLoanInfo, WhatsAppInsuranceInfo,
                               WhatsAppProspectInfo)
from import_export.admin import ImportExportModelAdmin

from .resource import (ReportResource, CustomerDetailsResource, WhatsAppCustomerResource, WhatsAppProspectInfoResource,
                       WhatsAppLoanInfoResource, WhatsAppInsuranceInfoResource)

from .models import Report
from django.utils.html import format_html




# @admin.register(CustomerDetails)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('vle_name', 'father_name_or_spouse_name', 'education', 'address_on_aadhar')
#     ordering = ('vle_name',)
#     search_fields = ('address_on_aadhar', 'education')
#     list_filter = ('education',)
#     list_editable = ('education', 'address_on_aadhar')
#
#     def edit_button_description(self, obj):
#         return format_html('<button class="edit-button" type="button">Edit</button> {}'.format(obj.description))
#
#     edit_button_description.short_description = 'Description with Edit'


class ReportAdmin(ImportExportModelAdmin):
    resource_class = ReportResource


admin.site.register(Report, ReportAdmin)


# class CustomerDetailAdmin(ImportExportModelAdmin):
#     resource_class = CustomerDetailsResource
#
#
# admin.site.register(CustomerDetails, CustomerDetailAdmin)


class WhatsAppCustomerAdmin(ImportExportModelAdmin):
    resource_class = WhatsAppCustomerResource


admin.site.register(WhatsAppCustomer, WhatsAppCustomerAdmin)


class WhatsAppProspectInfoAdmin(ImportExportModelAdmin):
    resource_class = WhatsAppProspectInfoResource


admin.site.register(WhatsAppProspectInfo, WhatsAppProspectInfoAdmin)


class WhatsAppLoanInfoAdmin(ImportExportModelAdmin):
    resource_class = WhatsAppLoanInfoResource


admin.site.register(WhatsAppLoanInfo, WhatsAppLoanInfoAdmin)


class WhatsAppInsuranceInfoAdmin(ImportExportModelAdmin):
    resource_class = WhatsAppInsuranceInfoResource


admin.site.register(WhatsAppInsuranceInfo, WhatsAppInsuranceInfoAdmin)

