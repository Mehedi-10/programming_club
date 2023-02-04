# Generated by Django 4.1.5 on 2023-02-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProgrammingClub', '0003_alter_atcoder_last_update_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atcoder',
            name='info',
            field=models.CharField(blank=True, default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='codechef',
            name='info',
            field=models.CharField(blank=True, default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='codeforces',
            name='info',
            field=models.CharField(blank=True, default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='atcoder_handle',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='cc_handle',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='cf_handle',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='loj_handle',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='toph_handle',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lightoj',
            name='info',
            field=models.CharField(blank=True, default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='toph',
            name='info',
            field=models.CharField(blank=True, default=None, max_length=10000, null=True),
        ),
    ]