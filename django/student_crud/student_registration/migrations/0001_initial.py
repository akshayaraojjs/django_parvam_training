# Generated by Django 4.2 on 2025-03-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('usn', models.CharField(max_length=10, unique=True)),
                ('branch', models.CharField(choices=[('CS', 'Computer Science'), ('EC', 'Electronics & Communication'), ('ME', 'Mechanical'), ('CV', 'Civil')], max_length=50)),
                ('sem', models.IntegerField()),
                ('course', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('email_id', models.EmailField(max_length=254)),
                ('hobbies', models.JSONField(default=list)),
                ('address', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('resume_pdf', models.FileField(blank=True, null=True, upload_to='pdfs/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
