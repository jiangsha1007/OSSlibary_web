from django.shortcuts import render,redirect
from django.http import HttpResponse
from model.community import *
from model.oss import *
from view.common import *
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
    if commit_yearmonth.count() > 0:
        for per_commit_yearmonth in commit_yearmonth:
            line_commit_data += str(per_commit_yearmonth.commits_count) + ','
            line_commit_arr += per_commit_yearmonth.yearmonth + ','

    extra_info.update({'line_commit_arr': line_commit_arr})
    extra_info.update({'line_commit_data': line_commit_data})
    return render(request, 'commit.html', extra_info)