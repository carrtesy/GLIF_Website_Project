# Generated by Django 2.1.5 on 2019-01-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20190114_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='workplace',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='birthdate',
            field=models.DateField(default='2000-01-01'),
        ),
    ]