# Generated by Django 3.0.3 on 2020-02-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule_based_engine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='camp_rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_name', models.CharField(max_length=15)),
                ('campaign', models.CharField(max_length=20)),
                ('condition', models.CharField(max_length=50)),
                ('action', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=5)),
                ('Start_time', models.DateTimeField()),
                ('schedule_time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='user_profile_info',
        ),
    ]
