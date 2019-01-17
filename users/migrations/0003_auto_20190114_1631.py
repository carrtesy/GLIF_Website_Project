# Generated by Django 2.1.5 on 2019-01-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190114_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthdate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phonenumber',
            field=models.CharField(default='010-0000-0000', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='self_intro',
            field=models.TextField(default='self_intro', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='year_in_school',
            field=models.CharField(choices=[('OB', 'OB'), ('1기', '1기'), ('2기', '2기'), ('3기', '3기'), ('4기', '4기')], default='4기', max_length=2),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name_en',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name_kr',
            field=models.CharField(max_length=250),
        ),
    ]