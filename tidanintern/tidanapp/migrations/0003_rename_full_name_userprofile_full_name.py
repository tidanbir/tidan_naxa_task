# Generated by Django 4.1.1 on 2022-09-21 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidanapp', '0002_rename_first_name_userprofile_full_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Full_name',
            new_name='full_name',
        ),
    ]