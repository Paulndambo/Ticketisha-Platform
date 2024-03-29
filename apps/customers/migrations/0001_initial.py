# Generated by Django 3.2.6 on 2023-01-25 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=255)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='customer_logos')),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('headquarters', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(default='active', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
