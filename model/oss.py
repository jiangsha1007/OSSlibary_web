from django.db import models


class OsslibMeta(models.Model):
    oss_id = models.BigIntegerField(unique=True)
    oss_from = models.IntegerField()
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
    oss_line_count = models.IntegerField()
    oss_developer_count = models.IntegerField()
    oss_file_count = models.IntegerField()
    oss_commit_count = models.IntegerField()
    oss_lastupdate_time = models.CharField(max_length=50)
    oss_owner_id = models.IntegerField()
    oss_owner_type = models.CharField(max_length=100)
    oss_fork = models.IntegerField()
    oss_star = models.IntegerField()
    oss_main_language = models.CharField(max_length=50)
    oss_owner_id = models.IntegerField()
    oss_owner_type = models.CharField(max_length=11)
    oss_size = models.IntegerField()
    oss_lastupdate_time = models.CharField(max_length=50)
    has_wiki = models.IntegerField()
    readme = models.CharField(max_length=5000)
    uid = models.IntegerField()
    status = models.IntegerField()
    update_time = models.CharField(max_length=50)
    oss_all_day = models.IntegerField()
    oss_active_day = models.IntegerField()
    oss_language = models.CharField(max_length=1000)
    f1 = models.FloatField()
    f2 = models.FloatField()
    f3 = models.FloatField()
    f4 = models.FloatField()
    f5 = models.FloatField()
    f6 = models.FloatField()
    score = models.FloatField()
    def __str__(self):
        return self.oss_fullname

    class Meta:
        db_table = 'osslib_metadata_2'


class OsslibTopic(models.Model):
    oss_id = models.BigIntegerField()
    topic = models.CharField(max_length=200)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'osslib_topic'


class OsslibIssue(models.Model):
    issue_user_type = models.IntegerField()
    issue_state = models.IntegerField()
    oss = models.ForeignKey(to='OsslibMeta',to_field='oss_id',on_delete='models.CASCADE')
    user_id = models.BigIntegerField()
    issue_close_time = models.CharField(max_length=100)
    issue_create_time = models.CharField(max_length=100)
    update_time = models.CharField(max_length=100)
    issue_comment_count = models.IntegerField()
    issue_id = models.IntegerField(unique=True, primary_key=True)
    issue_number = models.IntegerField()
    issue_update_time = models.CharField(max_length=100)
    issue_body = models.TextField()
    issue_title = models.TextField()

    def __str__(self):
        return self.issue_body

    class Meta:
        db_table = 'osslib_issue'
        ordering = ['-issue_create_time']


class OsslibPulls(models.Model):
    pull_id = models.IntegerField()
    pull_number = models.IntegerField()
    pull_state = models.IntegerField()
    pull_author_association = models.CharField(max_length=100)
    pull_create_time = models.CharField(max_length=100)
    pull_update_time = models.CharField(max_length=100)
    pull_closed_time = models.CharField(max_length=100)
    pull_merged_time = models.CharField(max_length=100)
    pull_is_merged = models.IntegerField()
    update_time = models.CharField(max_length=100)
    user_id = models.IntegerField()
    oss = models.ForeignKey(to='OsslibMeta', to_field='oss_id', on_delete='models.CASCADE')
    pull_title = models.TextField()
    pull_body = models.TextField()
    pull_is_reviewed = models.IntegerField()
    pull_comments = models.IntegerField()
    review_comments = models.IntegerField()
    request_reviewer = models.TextField()

    def __str__(self):
        return self.pull_body

    class Meta:
        db_table = 'osslib_pulls'
        ordering = ['-pull_create_time']


class OsslibStatistic(models.Model):
    community_id = models.IntegerField()
    issue_count = models.IntegerField()
    issue_comment_count = models.IntegerField()
    issue_close_count = models.IntegerField()
    issue_close_time = models.FloatField()
    core_issue_count = models.IntegerField()
    pull_count = models.IntegerField()
    pull_merged_count = models.IntegerField()
    pull_comment_count = models.IntegerField()
    pull_review_count = models.IntegerField()
    pull_review_comment_count = models.IntegerField()
    core_pull_count = models.IntegerField()
    pull_merged_time = models.FloatField()
    core_developer_count = models.IntegerField()
    loc = models.IntegerField()
    doc = models.IntegerField()
    foc = models.IntegerField()
    coc = models.IntegerField()
    fork_count = models.IntegerField()
    star_count = models.IntegerField()
    core_developer_change = models.FloatField()
    pull_change = models.FloatField()
    issue_change = models.FloatField()
    update_time = models.CharField(max_length=100)
    language_count = models.IntegerField()
    all_days = models.IntegerField()
    active_days = models.IntegerField()

    class Meta:
        db_table = 'osslib_statistic'
        ordering = ['-update_time']


class osslib_statistic_commit_yearmonth(models.Model):
    community_id = models.IntegerField()
    yearmonth = models.CharField(max_length=100)
    commits_count = models.IntegerField()

    class Meta:
        db_table = 'osslib_statistic_commit_yearmonth'
        ordering = ['yearmonth']


class osslib_statistic_issue_yearmonth(models.Model):
    community_id = models.IntegerField()
    yearmonth = models.CharField(max_length=100)
    issue_count = models.IntegerField()
    close_issue_count = models.IntegerField()

    class Meta:
        db_table = 'osslib_statistic_issue_yearmonth'
        ordering = ['yearmonth']


class osslib_statistic_pull_yearmonth(models.Model):
    community_id = models.IntegerField()
    yearmonth = models.CharField(max_length=100)
    pull_count = models.IntegerField()
    merged_pull_count = models.IntegerField()

    class Meta:
        db_table = 'osslib_statistic_pull_yearmonth'
        ordering = ['yearmonth']


class osslib_statistic_commit_hourday(models.Model):
    community_id = models.IntegerField()
    day = models.IntegerField()
    commit_count = models.IntegerField()
    hour = models.IntegerField()

    class Meta:
        db_table = 'osslib_statistic_commit_hourday'
        ordering = ['day', 'hour']