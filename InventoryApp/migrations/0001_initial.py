# Generated by Django 3.2 on 2021-04-15 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('issued', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AccessRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_request', models.CharField(choices=[('Sent', 'Sent'), ('Accepted', 'Accepted'), ('Denied', 'Denied')], max_length=10)),
                ('user_type', models.CharField(choices=[('Employee', 'Employee'), ('Manager', 'Manager')], max_length=10)),
                ('issued_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InventoryApp.equipment')),
            ],
        ),
    ]