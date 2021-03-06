# Generated by Django 4.0 on 2021-12-23 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_users_nationality'),
        ('mongapp', '0002_alter_record_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='cal',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='record',
            name='hour',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='record',
            name='min',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='record',
            name='walk',
            field=models.CharField(max_length=10000),
        ),
        migrations.CreateModel(
            name='MongUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monguser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.users', verbose_name='현유저')),
            ],
        ),
    ]
