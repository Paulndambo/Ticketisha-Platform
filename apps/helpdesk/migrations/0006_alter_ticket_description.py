# Generated by Django 4.1.1 on 2023-02-18 08:18

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0005_alter_ticket_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=django_quill.fields.QuillField(),
        ),
    ]