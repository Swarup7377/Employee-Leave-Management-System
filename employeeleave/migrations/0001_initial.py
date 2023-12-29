# Generated by Django 3.0.3 on 2020-10-25 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptname', models.CharField(max_length=100)),
                ('deptshortname', models.CharField(max_length=15)),
                ('deptcode', models.CharField(max_length=10)),
                ('creationdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('phoneno', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=15, null=True)),
                ('regdate', models.DateField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leavetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leavetypename', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=500)),
                ('creationdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Leaves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todate', models.DateField()),
                ('fromdate', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('postingdate', models.DateField()),
                ('adminremark', models.CharField(max_length=100)),
                ('adminremarkdate', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('isread', models.CharField(max_length=50)),
                ('emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employeeleave.Employee')),
                ('leavetype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employeeleave.Leavetype')),
            ],
        ),
    ]
