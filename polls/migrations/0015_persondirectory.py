# Generated by Django 2.1.1 on 2018-10-24 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20181024_0452'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonDirectory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('come_num', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Person')),
            ],
        ),
    ]
