# Generated by Django 3.0.8 on 2020-08-09 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0002_auto_20200809_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='user_profile',
            field=models.ForeignKey(db_column='user_profile', on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile'),
        ),
    ]
