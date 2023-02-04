# Generated by Django 4.1.5 on 2023-02-03 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProgrammingClub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='toph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=10000, null=True)),
                ('last_update_time', models.TimeField()),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProgrammingClub.contestant')),
            ],
        ),
        migrations.CreateModel(
            name='lightoj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=10000, null=True)),
                ('last_update_time', models.TimeField()),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProgrammingClub.contestant')),
            ],
        ),
        migrations.CreateModel(
            name='codeforces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=10000, null=True)),
                ('last_update_time', models.TimeField()),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProgrammingClub.contestant')),
            ],
        ),
        migrations.CreateModel(
            name='codechef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=10000, null=True)),
                ('last_update_time', models.TimeField()),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProgrammingClub.contestant')),
            ],
        ),
    ]