# Generated by Django 2.1.5 on 2019-01-28 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20190127_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glifer',
            name='profile_img',
            field=models.FileField(default='./static/users/man-user.png', upload_to='profiles/%Y/%m/%d/'),
        ),
    ]
