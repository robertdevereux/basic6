# Generated by Django 5.1 on 2024-10-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBTest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('colour', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'basic5_dbtest',
            },
        ),
    ]
