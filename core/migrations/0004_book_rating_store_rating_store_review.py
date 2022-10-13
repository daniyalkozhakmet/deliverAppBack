# Generated by Django 4.1.2 on 2022-10-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_book_transaction_book_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.FloatField(blank=True, default='5', null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='rating',
            field=models.FloatField(blank=True, default='5', null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='review',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
