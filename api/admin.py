from django.contrib import admin
from django.apps import apps
from .models import *


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'address',
        'formatted_address',
        'addressline',
        'admindistrict',
        'countryregion',
        'city',
        'zip_code',
    )

class AttachmentRelationsAdmin(admin.ModelAdmin):
    list_display = (
        'instance_type',
        'instance_id',
        'attachment_id',
        'type'
    )

class AttachmentsAdmin(admin.ModelAdmin):
    list_display = (
        'original_name',
        'stored_name',
        'size'
    )

class CitiesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        'state',
        'county',
        'lat',
        'lng',
        'aid'
    )

class CountiesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        'state',
    )

class CustomerContactsAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'name',
        'phone',
        'email',
        'fax',
        'primary',
    )

class CustomersAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        'city',
        'state',
        'country',
        'line1',
        'line2',
        'zip',
        'phone',
        'mcnumber',
        'currency',
    )

class DictionariesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description'
    )

class DictionaryValuesAdmin(admin.ModelAdmin):
    list_display = (
        'dictionary',
        'code',
        'text'
    )

class DistanceAdmin(admin.ModelAdmin):
    list_display = (
        'distance',
        'from_field',
        'to',
    )

class DriversAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'birth_date',
        'address',
        'active',
        'status',
        'license_type',
        'license_expires_at',
        'driver_since_year',
        'operator',
        'trailer',
        'power_unit',
    )

class FailedJobdsAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'connection',
        'queue',
        'payload',
        'exception',
        'failed_at'
    )

class InvoicesAdmin(admin.ModelAdmin):
    list_display = (
        'load_id',
        'status',
        'invoice_id',
    )

class LoadsAdmin(admin.ModelAdmin):
    list_display = (
        'driver',
        'delivery_status',
        'driver_status',
        'power_unit',
        'trailer',
        'customer',
        'pickup_address',
        'delivery_address',
        'order_number',
        'distance',
        'tonu',
        'price',
        'netamount'
    )


class PowerUnitsAdmin(admin.ModelAdmin):
    list_display = (
        'model',
        'pu_number',
        'license_plate',
        'license_plate_expiration',
        'vehicle_id_number'
    )


class StatesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class TrailersAdmin(admin.ModelAdmin):
    list_display = (
        'model',
        'trailer_number',
        'type',
        'license_plate',
        'license_plate_expiration',
        'vehicle_id_number',
        'dot_expiration',
        'inspection_expiration',
        'active',
    )



class ZipsAdmin(admin.ModelAdmin):
    list_display = (
        'zip',
        'city',
        'state',
        'county'
    )



admin.site.register(Addresses, AddressAdmin)
admin.site.register(AttachmentRelations, AttachmentRelationsAdmin)
admin.site.register(Attachments, AttachmentsAdmin)
admin.site.register(Cities, CitiesAdmin)
admin.site.register(Counties, CountiesAdmin)
admin.site.register(CustomerContacts, CustomerContactsAdmin)
admin.site.register(Customers, CustomersAdmin)
admin.site.register(Dictionaries,DictionariesAdmin)
admin.site.register(DictionaryValues, DictionaryValuesAdmin)
admin.site.register(Distances, DistanceAdmin)
admin.site.register(Drivers, DriversAdmin)
admin.site.register(FailedJobs, FailedJobdsAdmin)
admin.site.register(Invoices, InvoicesAdmin)
admin.site.register(Loads, LoadsAdmin)
admin.site.register(PowerUnits, PowerUnitsAdmin)
admin.site.register(States, StatesAdmin)
admin.site.register(Trailers, TrailersAdmin)



admin.site.register(Zips, ZipsAdmin)

