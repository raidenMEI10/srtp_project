from django.db import models


# 对数据库操作
# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(max_length=10, default=20)


class AllRecordsG18(models.Model):
    file_name = models.CharField(db_column='File_Name', max_length=30, blank=True,
                                 null=True)  # Field name made lowercase.
    data_id = models.IntegerField(db_column='Data_Id', primary_key=True)  # Field name made lowercase.
    door_no = models.CharField(db_column='Door_No', max_length=20, blank=True, null=True)  # Field name made lowercase.
    device_sn = models.CharField(db_column='Device_Sn', max_length=30, blank=True,
                                 null=True)  # Field name made lowercase.
    get_time = models.DateTimeField(db_column='Get_Time', blank=True, null=True)  # Field name made lowercase.
    is_opendoor = models.IntegerField(db_column='Is_OpenDoor', blank=True, null=True)  # Field name made lowercase.
    is_fault = models.IntegerField(db_column='Is_Fault', blank=True, null=True)  # Field name made lowercase.
    is_normal = models.IntegerField(db_column='Is_Normal', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationId', blank=True, null=True)  # Field name made lowercase.
    updown = models.IntegerField(db_column='UpDown', blank=True, null=True)  # Field name made lowercase.
    original_speeddata = models.CharField(db_column='Original_SpeedData', max_length=200, blank=True,
                                          null=True)  # Field name made lowercase.
    original_torquedata = models.CharField(db_column='Original_TorqueData', max_length=200, blank=True,
                                           null=True)  # Field name made lowercase.
    original_angledata = models.CharField(db_column='Original_AngleData', max_length=200, blank=True,
                                          null=True)  # Field name made lowercase.
    original_temperaturedata = models.CharField(db_column='Original_TemperatureData', max_length=200, blank=True,
                                                null=True)  # Field name made lowercase.
    change_speeddata = models.CharField(db_column='Change_SpeedData', max_length=200, blank=True,
                                        null=True)  # Field name made lowercase.
    change_torquedata = models.CharField(db_column='Change_TorqueData', max_length=200, blank=True,
                                         null=True)  # Field name made lowercase.
    change_angledata = models.CharField(db_column='Change_AngleData', max_length=200, blank=True,
                                        null=True)  # Field name made lowercase.
    change_temperaturedata = models.CharField(db_column='Change_TemperatureData', max_length=200, blank=True,
                                              null=True)  # Field name made lowercase.
    dcu_data = models.CharField(db_column='DCU_Data', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    datacreated = models.DateTimeField(db_column='DataCreated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'all_records_g18'
