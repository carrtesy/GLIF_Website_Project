# Generated by Django 2.1.5 on 2019-02-08 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_auto_20190208_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glifer',
            name='nth',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Nth'),
        ),
    ]
