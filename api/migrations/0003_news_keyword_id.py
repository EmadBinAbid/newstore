# Generated by Django 2.2.13 on 2020-06-26 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='keyword_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Keywords'),
            preserve_default=False,
        ),
    ]
