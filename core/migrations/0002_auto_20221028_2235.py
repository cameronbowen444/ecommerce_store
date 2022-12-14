# Generated by Django 2.2.4 on 2022-10-28 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('B', 'Bars'), ('P', 'Weights And Plates'), ('E', 'Equipment'), ('C', 'Conditioning'), ('S', 'Storage'), ('G', 'Gear'), ('A', 'Accessories'), ('SH', 'Shoes'), ('AP', 'Apparel'), ('SU', 'Suppliments')], default='B', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='P', max_length=2),
            preserve_default=False,
        ),
    ]
