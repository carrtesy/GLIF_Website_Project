# Generated by Django 2.1.5 on 2019-02-07 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0039_auto_20190204_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glifer',
            name='nth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Nth'),
        ),
    ]