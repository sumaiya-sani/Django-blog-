# Generated by Django 4.0.2 on 2022-03-07 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0013_alter_profile_facebook_url_alter_profile_githube_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50),
        ),
    ]
