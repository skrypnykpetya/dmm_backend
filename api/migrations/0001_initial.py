# Generated by Django 4.0.4 on 2022-04-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('formatted_address', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('addressline', models.CharField(blank=True, db_column='addressLine', max_length=255, null=True)),
                ('admindistrict', models.CharField(blank=True, db_column='adminDistrict', max_length=255, null=True)),
                ('admindistrict2', models.CharField(blank=True, db_column='adminDistrict2', max_length=255, null=True)),
                ('countryregion', models.CharField(blank=True, db_column='countryRegion', max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'addresses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttachmentRelations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('instance_type', models.CharField(max_length=255)),
                ('instance_id', models.PositiveBigIntegerField()),
                ('attachment_id', models.PositiveBigIntegerField()),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'attachment_relations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.PositiveBigIntegerField()),
                ('original_name', models.CharField(max_length=255)),
                ('stored_name', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'attachments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('lat', models.DecimalField(decimal_places=4, max_digits=7)),
                ('lng', models.DecimalField(decimal_places=4, max_digits=7)),
                ('aid', models.PositiveBigIntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'counties',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerContacts',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('fax', models.CharField(blank=True, max_length=255, null=True)),
                ('primary', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customer_contacts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('line1', models.CharField(max_length=255)),
                ('line2', models.CharField(blank=True, max_length=255, null=True)),
                ('zip', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('mcnumber', models.CharField(db_column='mcNumber', max_length=255)),
                ('currency', models.CharField(max_length=255)),
                ('debtorid', models.PositiveBigIntegerField(blank=True, db_column='debtorId', null=True)),
                ('areoriginalsrequired', models.IntegerField(db_column='areOriginalsRequired')),
                ('isduplicatematchdebtortext', models.IntegerField(db_column='isDuplicateMatchDebtorText')),
                ('isfirstuse', models.IntegerField(db_column='isFirstUse')),
                ('lastuseddate', models.DateField(blank=True, db_column='lastUsedDate', null=True)),
                ('private_note', models.TextField(blank=True, null=True)),
                ('public_note', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dictionaries',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dictionaries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DictionaryValues',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dictionary_values',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Distances',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('distance', models.FloatField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'distances',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('active', models.IntegerField()),
                ('status', models.CharField(max_length=7)),
                ('license_type', models.CharField(max_length=255)),
                ('license_expires_at', models.DateField()),
                ('driver_since_year', models.CharField(max_length=255)),
                ('years_experience', models.CharField(max_length=255)),
                ('cdl_number', models.CharField(max_length=255)),
                ('dot_medical_expiration', models.DateField(blank=True, null=True)),
                ('license_expiration', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'drivers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FailedJobs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(max_length=255, unique=True)),
                ('connection', models.TextField()),
                ('queue', models.TextField()),
                ('payload', models.TextField()),
                ('exception', models.TextField()),
                ('failed_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'failed_jobs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('load_id', models.PositiveBigIntegerField()),
                ('status', models.CharField(max_length=10)),
                ('invoice_id', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'invoices',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loads',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_number', models.CharField(max_length=255)),
                ('distance', models.IntegerField()),
                ('tonu', models.IntegerField()),
                ('price', models.CharField(max_length=255)),
                ('netamount', models.IntegerField(db_column='netAmount')),
                ('advance', models.IntegerField(blank=True, null=True)),
                ('advance_fee', models.IntegerField(blank=True, null=True)),
                ('lumper_fee', models.IntegerField(blank=True, null=True)),
                ('detention_pay', models.IntegerField(blank=True, null=True)),
                ('deduction', models.IntegerField(blank=True, null=True)),
                ('price_other', models.IntegerField(blank=True, null=True)),
                ('pickup_date', models.DateField(db_column='pickUp_date')),
                ('delivery_date', models.DateField()),
                ('pickup_time', models.CharField(blank=True, db_column='pickUp_time', max_length=255, null=True)),
                ('delivery_time', models.CharField(blank=True, max_length=255, null=True)),
                ('delivery_status', models.CharField(max_length=10)),
                ('payment_status', models.CharField(max_length=9)),
                ('driver_status', models.CharField(max_length=20)),
                ('reference_number', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'loads',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PowerUnits',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=255)),
                ('pu_number', models.CharField(max_length=255)),
                ('license_plate', models.CharField(max_length=255)),
                ('license_plate_expiration', models.DateField()),
                ('vehicle_id_number', models.CharField(max_length=255)),
                ('dot_expiration', models.DateField(blank=True, null=True)),
                ('inspection_expiration', models.DateField(blank=True, null=True)),
                ('active', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'power_units',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'states',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trailers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=255)),
                ('trailer_number', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('license_plate', models.CharField(max_length=255)),
                ('license_plate_expiration', models.DateField()),
                ('vehicle_id_number', models.CharField(max_length=255)),
                ('dot_expiration', models.DateField(blank=True, null=True)),
                ('inspection_expiration', models.DateField(blank=True, null=True)),
                ('active', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'trailers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zips',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('zip', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'zips',
                'managed': False,
            },
        ),
    ]
