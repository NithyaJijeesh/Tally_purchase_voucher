# Generated by Django 4.1 on 2023-10-20 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_rename_credit_amount_purchase_particulars_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase_voucher',
            name='company',
        ),
        migrations.RemoveField(
            model_name='purchase_voucher',
            name='voucher',
        ),
        migrations.RemoveField(
            model_name='receipt_note_no',
            name='purchase',
        ),
        migrations.DeleteModel(
            name='purchase_particulars',
        ),
        migrations.DeleteModel(
            name='purchase_voucher',
        ),
        migrations.DeleteModel(
            name='receipt_note_no',
        ),
    ]