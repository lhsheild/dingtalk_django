# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class DingCallbackFlowinfo(models.Model):
    people = models.CharField(max_length=32)
    flow_date = models.DateField()
    flow_time = models.TimeField()
    time1 = models.FloatField(blank=True, null=True)
    volume1 = models.FloatField(blank=True, null=True)
    time2 = models.FloatField(blank=True, null=True)
    volume2 = models.FloatField(blank=True, null=True)
    time3 = models.FloatField(blank=True, null=True)
    volume3 = models.FloatField(blank=True, null=True)
    diameter = models.FloatField(blank=True, null=True)
    mud_depth = models.FloatField(blank=True, null=True)
    cicle_lequid_level1 = models.FloatField(blank=True, null=True)
    cicle_instantaneous_flow_rate1 = models.FloatField(blank=True, null=True)
    cicle_lequid_level2 = models.FloatField(blank=True, null=True)
    cicle_instantaneous_flow_rate2 = models.FloatField(blank=True, null=True)
    cicle_lequid_level3 = models.FloatField(blank=True, null=True)
    cicle_instantaneous_flow_rate3 = models.FloatField(blank=True, null=True)
    canal_width = models.FloatField(blank=True, null=True)
    square_lequid_level1 = models.FloatField(blank=True, null=True)
    square_instantaneous_flow_rate1 = models.FloatField(blank=True, null=True)
    square_lequid_level2 = models.FloatField(blank=True, null=True)
    square_instantaneous_flow_rate2 = models.FloatField(blank=True, null=True)
    square_lequid_level3 = models.FloatField(blank=True, null=True)
    square_instantaneous_flow_rate3 = models.FloatField(blank=True, null=True)
    machine_flow = models.FloatField(blank=True, null=True)
    monitor_point = models.ForeignKey('DingCallbackMonitorpoint', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'ding_callback_flowinfo'


class DingCallbackMonitorpoint(models.Model):
    name = models.CharField(max_length=64)
    geophysical_point = models.CharField(unique=True, max_length=64)
    is_monitor = models.IntegerField()
    not_monitor_reason = models.CharField(max_length=512, blank=True, null=True)
    work_function = models.IntegerField()
    exterior_photo = models.CharField(max_length=512, blank=True, null=True)
    water_flow_photo = models.CharField(max_length=512, blank=True, null=True)
    status_photo = models.CharField(max_length=512, blank=True, null=True)
    probe_photo = models.CharField(max_length=512, blank=True, null=True)
    machine_photo = models.CharField(max_length=512, blank=True, null=True)
    setup_photo = models.CharField(max_length=512, blank=True, null=True)
    work_photo = models.CharField(max_length=512, blank=True, null=True)
    people = models.CharField(max_length=32)
    start_time = models.DateField()

    class Meta:
        managed = True
        db_table = 'ding_callback_monitorpoint'


class DingCallbackSampleinfo(models.Model):
    people = models.CharField(max_length=32)
    sample_date = models.DateField()
    sample_time = models.TimeField()
    sample_number = models.CharField(max_length=32)
    sample_photo = models.CharField(max_length=512)
    sample_color = models.CharField(max_length=32)
    sample_odor = models.CharField(max_length=32)
    sample_turbidity = models.CharField(max_length=32)
    ss = models.CharField(db_column='SS', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nh3_n = models.CharField(db_column='NH3_N', max_length=32, blank=True, null=True)  # Field name made lowercase.
    tp = models.CharField(db_column='TP', max_length=32, blank=True, null=True)  # Field name made lowercase.
    tn = models.CharField(db_column='TN', max_length=32, blank=True, null=True)  # Field name made lowercase.
    cod = models.CharField(db_column='COD', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bod = models.CharField(db_column='BOD', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ais = models.CharField(db_column='AIS', max_length=32, blank=True, null=True)  # Field name made lowercase.
    afvo = models.CharField(db_column='AFVO', max_length=32, blank=True, null=True)  # Field name made lowercase.
    do = models.CharField(db_column='DO', max_length=32, blank=True, null=True)  # Field name made lowercase.
    flow = models.CharField(db_column='FLOW', max_length=32, blank=True, null=True)  # Field name made lowercase.
    cr = models.CharField(db_column='CR', max_length=32, blank=True, null=True)  # Field name made lowercase.
    orp = models.CharField(db_column='ORP', max_length=32, blank=True, null=True)  # Field name made lowercase.
    sinkables = models.CharField(db_column='SinkableS', max_length=32, blank=True, null=True)  # Field name made lowercase.
    sulfide = models.CharField(db_column='Sulfide', max_length=32, blank=True, null=True)  # Field name made lowercase.
    cyanide = models.CharField(db_column='Cyanide', max_length=32, blank=True, null=True)  # Field name made lowercase.
    monitor_point = models.ForeignKey(DingCallbackMonitorpoint, models.DO_NOTHING)
    monitor_task = models.CharField(max_length=128)
    sample_count = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'ding_callback_sampleinfo'
