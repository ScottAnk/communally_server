# Generated by Django 3.2.12 on 2023-05-20 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=10000)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=5000)),
                ('votes', models.IntegerField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('replies_to', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='events.post')),
            ],
        ),
    ]
