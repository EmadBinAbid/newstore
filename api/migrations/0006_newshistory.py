# Generated by Django 2.2.13 on 2020-06-27 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200627_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
                ('source', models.CharField(max_length=60)),
                ('expiry_date', models.DateTimeField()),
                ('keyword_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Keywords')),
            ],
        ),
    ]
