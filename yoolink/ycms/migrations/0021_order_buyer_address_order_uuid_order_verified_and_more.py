# Generated by Django 4.0.10 on 2024-01-29 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ycms', '0020_message_title_alter_message_date_alter_message_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='buyer_address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='order',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(default=''),
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=255)),
                ('full_name', models.CharField(default='', max_length=255)),
                ('company_name', models.CharField(default='', max_length=255)),
                ('tel_number', models.CharField(default='', max_length=18)),
                ('fax_number', models.CharField(default='', max_length=18)),
                ('mobile_number', models.CharField(default='', max_length=18)),
                ('website', models.URLField(blank=True, default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
