# Generated by Django 2.1.5 on 2019-01-17 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date_of_birth', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(default='2000-01-01')),
                ('phonenumber', models.CharField(max_length=250)),
                ('self_intro', models.TextField(max_length=1000)),
                ('email', models.EmailField(max_length=250)),
                ('studentid', models.CharField(max_length=50)),
                ('schyr', models.CharField(choices=[(1, '1학년'), (2, '2학년'), (3, '3학년'), (4, '4학년'), (0, '기타')], default=1, max_length=10)),
                ('schsem', models.CharField(choices=[(1, '1학년'), (2, '2학년'), (3, '3학년'), (4, '4학년'), (0, '기타')], default=1, max_length=10)),
                ('schyr_grad', models.CharField(max_length=250)),
                ('extracurr', models.TextField(max_length=5000)),
                ('testprep', models.TextField(max_length=1000)),
                ('willyou', models.CharField(max_length=50)),
                ('millitary', models.CharField(max_length=50)),
                ('glifmotive', models.TextField(max_length=5000)),
                ('futureplan', models.TextField(max_length=5000)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to='recruiting.Applicant')),
            ],
        ),
    ]