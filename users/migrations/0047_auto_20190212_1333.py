# Generated by Django 2.1.5 on 2019-02-12 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0046_auto_20190209_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glifer',
            name='career',
        ),
        migrations.RemoveField(
            model_name='glifer',
            name='self_intro_add',
        ),
        migrations.DeleteModel(
            name='Career',
        ),
    ]
