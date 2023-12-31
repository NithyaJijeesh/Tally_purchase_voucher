# Generated by Django 4.1 on 2023-09-28 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_receipt_note_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase_particulars',
            old_name='credit_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='purchase_particulars',
            old_name='particular',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='purchase_particulars',
            old_name='debit_amount',
            new_name='item_id',
        ),
        migrations.RenameField(
            model_name='purchase_particulars',
            old_name='particular_id',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='purchase_voucher',
            old_name='particulars',
            new_name='address',
        ),
        migrations.AddField(
            model_name='purchase_particulars',
            name='per',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchase_particulars',
            name='rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='bill_of_lading',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='carriername_agent',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='destination',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='dispatched_through',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='gst_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='gst_treatment',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='mailing_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='motor_vehicle_no',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='party_accname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='purchase_ledger',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='receipt_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='receipt_doc_no',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='state',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='sup_inv_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchase_voucher',
            name='supplier',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
