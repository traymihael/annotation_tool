# Generated by Django 2.1.1 on 2018-10-24 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_dirtargetindx'),
    ]

    operations = [
        migrations.RenameField(
            model_name='targetindex',
            old_name='index',
            new_name='index_num',
        ),
    ]