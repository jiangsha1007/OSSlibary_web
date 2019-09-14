from django.shortcuts import render,redirect
from django.http import HttpResponse
from model.community import *
from model.oss import *
from view.common import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from operator import itemgetter

def commit(request):
    extra_info = dict()
    uid = request.session['user_id']
    community = get_nav_list(uid)
    extra_info.update(community)
    cid = request.GET.get('cid')
    commit_yearmonth = osslib_statistic_commit_yearmonth.objects.filter(community_id=int(cid))
    line_commit_arr = ''
    line_commit_data = ''
    line_issue_close_data = ''
    if commit_yearmonth.count() > 0:
        for per_commit_yearmonth in commit_yearmonth:
            line_commit_data += str(per_commit_yearmonth.commits_count) + ','
            line_commit_arr += per_commit_yearmonth.yearmonth + ','

    issue_yearmonth = osslib_statistic_issue_yearmonth.objects.filter(community_id=int(cid))
    line_issue_arr = ''
    line_issue_data = ''
    if issue_yearmonth.count() > 0:
        for per_issue_yearmonth in issue_yearmonth:
            line_issue_data += str(per_issue_yearmonth.issue_count) + ','
            line_issue_arr += per_issue_yearmonth.yearmonth + ','
            line_issue_close_data += str(per_issue_yearmonth.close_issue_count) + ','

    pull_yearmonth = osslib_statistic_pull_yearmonth.objects.filter(community_id=int(cid))
    line_pull_arr = ''
    line_pull_data = ''
    line_pull_merged_data = ''
    if issue_yearmonth.count() > 0:
        for per_pull_yearmonth in pull_yearmonth:
            line_pull_data += str(per_pull_yearmonth.pull_count) + ','
            line_pull_arr += per_pull_yearmonth.yearmonth + ','
            line_pull_merged_data += str(per_pull_yearmonth.merged_pull_count) + ','

    commit_hourday = osslib_statistic_commit_hourday.objects.filter(community_id=int(cid))
    commit_hourday_arr = ''
    if commit_hourday.count() > 0:
        for per_commit_hourday in commit_hourday:
            commit_hourday_str = str(per_commit_hourday.day) + '-' + str(per_commit_hourday.hour) + '-' + str(per_commit_hourday.commit_count)
            commit_hourday_arr += commit_hourday_str+','
    print(commit_hourday_arr)
    extra_info.update({'line_commit_arr': line_commit_arr})
    extra_info.update({'line_commit_data': line_commit_data})
    extra_info.update({'line_issue_arr': line_issue_arr})
    extra_info.update({'line_issue_data': line_issue_data})
    extra_info.update({'line_issue_close_data': line_issue_close_data})

    extra_info.update({'line_pull_arr': line_pull_arr})
    extra_info.update({'line_pull_data': line_pull_data})
    extra_info.update({'line_pull_merged_data': line_pull_merged_data})
    extra_info.update({'commit_hourday': commit_hourday_arr[:-1]})
    return render(request, 'commit.html', extra_info)

def issue(request):
    extra_info = dict()
    uid = request.session['user_id']

    community = get_nav_list(uid)
    extra_info.update(community)
    cid = request.GET.get('cid')
    try:
        page = request.GET.get('page')
    except:
        page = 1
    oss_id = []
    oss_list_id = OsslibCommunityList.objects.values("oss_id").filter(community_id=int(cid))
    for per_oss_id in oss_list_id:
        oss_id.append(int(per_oss_id['oss_id']))

    issue_all = OsslibIssue.objects.filter(oss_id__in=oss_id)[0:100]
    paginator = Paginator(issue_all, 20)
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)

    issue_statistic = OsslibStatistic.objects.filter(community_id=int(cid))[0:1]
    issue_count = issue_statistic[0].issue_count
    issue_close_count = issue_statistic[0].issue_close_count
    issue_open_count = int(issue_count)-int(issue_close_count)

    extra_info.update({'issue': customer})
    extra_info.update({'cid': cid})
    extra_info.update({'issue_count': issue_count})
    extra_info.update({'issue_close_count': issue_close_count})
    extra_info.update({'issue_open_count': issue_open_count})
    return render(request, 'issue.html', extra_info)


def pull(request):
    extra_info = dict()
    uid = request.session['user_id']
    community = get_nav_list(uid)
    extra_info.update(community)
    cid = request.GET.get('cid')
    try:
        page = request.GET.get('page')
    except:
        page = 1
    oss_id = []
    oss_list_id = OsslibCommunityList.objects.values("oss_id").filter(community_id=int(cid))
    for per_oss_id in oss_list_id:
        oss_id.append(int(per_oss_id['oss_id']))

    pulls_all = OsslibPulls.objects.filter(oss_id__in=oss_id)[0:100]
    paginator = Paginator(pulls_all, 20)
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)

    pull_statistic = OsslibStatistic.objects.filter(community_id=int(cid))[0:1]
    pull_count = pull_statistic[0].pull_count
    pull_merged_count = pull_statistic[0].pull_merged_count
    pull_umerged_count = int(pull_count)-int(pull_merged_count)

    extra_info.update({'pull': customer})
    extra_info.update({'cid': cid})
    extra_info.update({'pull_count': pull_count})
    extra_info.update({'pull_merged_count': pull_merged_count})
    extra_info.update({'pull_umerged_count': pull_umerged_count})
    return render(request, 'pull.html', extra_info)