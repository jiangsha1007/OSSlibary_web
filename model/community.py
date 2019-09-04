from django.db import models
from model.oss import *

class OsslibCommunity(models.Model):
    user_id = models.IntegerField(max_length=11)
    community_name = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(max_length=11)
    class Meta:
        db_table = 'osslib_community'


class OsslibCommunityList(models.Model):
    community_id = models.IntegerField(max_length=11)
    oss_id = models.IntegerField(max_length=11)
    oss_name = models.CharField(max_length=256)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(max_length=11)
    class Meta:
        db_table = 'osslib_community_list'