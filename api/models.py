from django.db import models
from users.models import Users


class Trailers(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.CharField(max_length=255)
    trailer_number = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=255)
    license_plate_expiration = models.DateField()
    vehicle_id_number = models.CharField(max_length=255)
    dot_expiration = models.DateField(blank=True, null=True)
    inspection_expiration = models.DateField(blank=True, null=True)
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trailers'

    def __str__(self):
        return self.model


class Drivers(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    active = models.IntegerField()
    status = models.CharField(max_length=7)
    license_type = models.CharField(max_length=255)
    license_expires_at = models.DateField()
    driver_since_year = models.CharField(max_length=255)
    years_experience = models.CharField(max_length=255)
    cdl_number = models.CharField(max_length=255)
    dot_medical_expiration = models.DateField(blank=True, null=True)
    license_expiration = models.DateField(blank=True, null=True)
    operator = models.ForeignKey(Users, related_name='operator', on_delete=models.DO_NOTHING, blank=True, null=True)
    trailer = models.ForeignKey(Trailers, related_name='trailers', on_delete=models.DO_NOTHING, blank=True, null=True)
    power_unit = models.ForeignKey('PowerUnits', related_name='power_units', on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(Users, related_name='user', on_delete=models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drivers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'



class Customers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    mcnumber = models.CharField(db_column='mcNumber', max_length=255)  # Field name made lowercase.
    currency = models.CharField(max_length=255)
    debtorid = models.PositiveBigIntegerField(db_column='debtorId', blank=True, null=True)  # Field name made lowercase.
    areoriginalsrequired = models.IntegerField(db_column='areOriginalsRequired')  # Field name made lowercase.
    isduplicatematchdebtortext = models.IntegerField(db_column='isDuplicateMatchDebtorText')  # Field name made lowercase.
    isfirstuse = models.IntegerField(db_column='isFirstUse')  # Field name made lowercase.
    lastuseddate = models.DateField(db_column='lastUsedDate', blank=True, null=True)  # Field name made lowercase.
    weight = models.ForeignKey('DictionaryValues', related_name='weight', on_delete=models.DO_NOTHING, blank=True, null=True)
    distance = models.ForeignKey('DictionaryValues', related_name='distance', on_delete=models.DO_NOTHING, blank=True, null=True)
    temperature = models.ForeignKey('DictionaryValues', related_name='temperatur', on_delete=models.DO_NOTHING, blank=True, null=True)
    private_note = models.TextField(blank=True, null=True)
    public_note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'customers'

class CustomerContacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey('Customers', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    primary = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_contacts'

    def __str__(self):
        return self.name




class Addresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=255)
    formatted_address = models.CharField(unique=True, max_length=255, blank=True, null=True)
    addressline = models.CharField(db_column='addressLine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admindistrict = models.CharField(db_column='adminDistrict', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admindistrict2 = models.CharField(db_column='adminDistrict2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    countryregion = models.CharField(db_column='countryRegion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'

    def __str__(self):
        return self.address

class AttachmentRelations(models.Model):
    id = models.BigAutoField(primary_key=True)
    instance_type = models.CharField(max_length=255)
    instance_id = models.PositiveBigIntegerField()
    attachment_id = models.PositiveBigIntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachment_relations'

    def __str__(self):
        return self.instance_type

class Attachments(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    original_name = models.CharField(max_length=255)
    stored_name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachments'

    def __str__(self):
        return self.original_name


class Cities(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    state = models.ForeignKey('States', related_name='states',  on_delete=models.DO_NOTHING)
    county = models.ForeignKey('Counties', related_name='countys', on_delete=models.DO_NOTHING)
    lat = models.DecimalField(max_digits=7, decimal_places=4)
    lng = models.DecimalField(max_digits=7, decimal_places=4)
    aid = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'

    def __str__(self):
        return self.name

class Counties(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    state = models.ForeignKey('States', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counties'

    def __str__(self):
        return self.name

class Dictionaries(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dictionaries'

    def __str__(self):
        return self.name


class DictionaryValues(models.Model):
    id = models.BigAutoField(primary_key=True)
    dictionary = models.ForeignKey(Dictionaries, on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dictionary_values'

    def __str__(self):
        return self.text


class Distances(models.Model):
    id = models.BigAutoField(primary_key=True)
    distance = models.FloatField()
    from_field = models.ForeignKey(Addresses, related_name='from_field', on_delete=models.DO_NOTHING, db_column='from_id')  # Field renamed because it was a Python reserved word.
    to = models.ForeignKey(Addresses, related_name='to', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distances'

    def __str__(self):
        return self.distance


class Invoices(models.Model):
    id = models.BigAutoField(primary_key=True)
    load_id = models.PositiveBigIntegerField()
    status = models.CharField(max_length=10)
    invoice_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'

    def __str__(self):
        return self.status


class Loads(models.Model):
    id = models.BigAutoField(primary_key=True)
    driver = models.ForeignKey('Drivers', related_name='driver', on_delete=models.DO_NOTHING, blank=True, null=True)
    power_unit = models.ForeignKey('PowerUnits', related_name='power_unit', on_delete=models.DO_NOTHING, blank=True, null=True)
    trailer = models.ForeignKey('Trailers', related_name='trailer', on_delete=models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customers, related_name='customer', on_delete=models.DO_NOTHING, blank=True, null=True)
    pickup_address = models.ForeignKey(Addresses, related_name='pickup', on_delete=models.DO_NOTHING, db_column='pickUp_address_id')  # Field name made lowercase.
    delivery_address = models.ForeignKey(Addresses, related_name='delivery', on_delete=models.DO_NOTHING)
    order_number = models.CharField(max_length=255)
    distance = models.IntegerField()
    tonu = models.IntegerField()
    price = models.CharField(max_length=255)
    netamount = models.IntegerField(db_column='netAmount')  # Field name made lowercase.
    advance = models.IntegerField(blank=True, null=True)
    advance_fee = models.IntegerField(blank=True, null=True)
    lumper_fee = models.IntegerField(blank=True, null=True)
    detention_pay = models.IntegerField(blank=True, null=True)
    deduction = models.IntegerField(blank=True, null=True)
    price_other = models.IntegerField(blank=True, null=True)
    pickup_date = models.DateField(db_column='pickUp_date')  # Field name made lowercase.
    delivery_date = models.DateField()
    pickup_time = models.CharField(db_column='pickUp_time', max_length=255, blank=True, null=True)  # Field name made lowercase.
    delivery_time = models.CharField(max_length=255, blank=True, null=True)
    delivery_status = models.CharField(max_length=10)
    payment_status = models.CharField(max_length=9)
    driver_status = models.CharField(max_length=20)
    reference_number = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loads'


class PowerUnits(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.CharField(max_length=255)
    pu_number = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=255)
    license_plate_expiration = models.DateField()
    vehicle_id_number = models.CharField(max_length=255)
    dot_expiration = models.DateField(blank=True, null=True)
    inspection_expiration = models.DateField(blank=True, null=True)
    trailer = models.ForeignKey(Trailers, on_delete=models.DO_NOTHING, blank=True, null=True)
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'power_units'

    def __str__(self):
        return self.model

class States(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'

    def __str__(self):
        return self.name

class Zips(models.Model):
    id = models.BigAutoField(primary_key=True)
    zip = models.TextField()
    city = models.ForeignKey(Cities, related_name='city', on_delete=models.DO_NOTHING)
    state = models.ForeignKey(States, related_name='state', on_delete=models.DO_NOTHING)
    county = models.ForeignKey(Counties, related_name='county', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.zip

    class Meta:
        managed = False
        db_table = 'zips'

