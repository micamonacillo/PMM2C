# Generated by Django 5.0.6 on 2024-07-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_blood_type_item_hours_worked_per_week_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='student_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
