# Generated by Django 3.2.6 on 2023-02-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0002_alter_ticket_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='screenshots',
            field=models.ImageField(blank=True, null=True, upload_to='screenshots/'),
        ),
    ]
