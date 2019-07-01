from django.db import models


class OsslibMeta(models.Model):
    community_id = models.BigIntegerField()
    community_from = models.IntegerField(max_length=11)
    oss_name = models.CharField(max_length=50)
    oss_fullname = models.CharField(max_length=100, unique=True)
    oss_create_time = models.CharField(max_length=50)
    oss_git_url = models.CharField(max_length=200)
    oss_git_tool = models.CharField(max_length=30)
    oss_repo_url = models.CharField(max_length=200)
    oss_homepage = models.CharField(max_length=100)
    oss_license = models.CharField(max_length=100)
    oss_description = models.TextField()
    oss_local_path = models.CharField(max_length=50)
    oss_line_count = models.IntegerField(max_length=50)
    oss_developer_count = models.IntegerField(max_length=50)
    oss_file_count = models.IntegerField(max_length=50)
    oss_commit_count = models.IntegerField(max_length=50)
    oss_lastupdate_time = models.CharField(max_length=50)
    oss_owner_id = models.IntegerField(max_length=50)
    oss_owner_type = models.CharField(max_length=100)
    oss_star = models.IntegerField(max_length=11)
    oss_main_language = models.CharField(max_length=50)
    oss_owner_id = models.IntegerField(max_length=11)
    oss_owner_type = models.CharField(max_length=11)
    oss_size = models.IntegerField(max_length=11)
    oss_lastupdate_time = models.CharField(max_length=50)
    has_wiki = models.IntegerField(max_length=11)
    readme = models.CharField(max_length=5000)

    def __str__(self):
        return self.oss_fullname

    class Meta:
        db_table = 'osslib_metadata'


class OsslibTopic(models.Model):
    oss_id = models.BigIntegerField()
    topic = models.CharField(max_length=200)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'osslib_topic'