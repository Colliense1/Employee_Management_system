# Generated by Django 5.1.1 on 2024-09-12 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_designation_alter_employee_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.CharField(max_length=10),
        ),
    ]