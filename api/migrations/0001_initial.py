# Generated by Django 2.2.13 on 2020-06-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=60)),
            ],
        ),
    ]
