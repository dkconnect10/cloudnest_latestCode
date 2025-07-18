# Generated by Django 4.2.23 on 2025-07-13 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_hospital_license'),
        ('users', '0005_userdetails_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.role')),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userdetails')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserHospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userdetails')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userhospital'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userrole'),
        ),
    ]
