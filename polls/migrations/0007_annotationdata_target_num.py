# Generated by Django 2.1.1 on 2018-10-03 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_annotationdata_target_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationdata',
            name='target_num',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.TargetData'),
            preserve_default=False,
        ),
    ]
