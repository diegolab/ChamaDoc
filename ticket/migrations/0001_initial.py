# Generated by Django 5.1.7 on 2025-03-12 22:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.CharField(max_length=15, unique=True)),
                ('ticket_title', models.CharField(max_length=50)),
                ('ticket_description', models.TextField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending', max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_resolved', models.BooleanField(default=False)),
                ('severity', models.CharField(choices=[('A', 'A'), ('B', 'B')], default='B', max_length=20)),
                ('contact_mode', models.CharField(choices=[('Phone', 'Phone'), ('Email', 'Email')], max_length=20)),
                ('is_assigned_to_engineer', models.BooleanField(default=False)),
                ('resolution_steps', models.TextField(blank=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='engineer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
