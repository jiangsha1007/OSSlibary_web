from django.shortcuts import render,redirect
from django.http import HttpResponse
from model.community import *
from model.oss import *
from view.common import *


def overview(request):
    extra_info = dict()
    uid = request.session['user_id']
    community = get_nav_list(uid)
    extra_info.update(community)
    cid = request.GET.get('cid')
    oss_list = OsslibCommunityList.objects.filter(community_id=int(cid))
    count_line = 0
    count_file = 0
    count_commit = 0
    count_developer = 0
    for per_oss_list in oss_list:
        oss_meta = OsslibMeta.objects.get(community_id=per_oss_list.oss_id)
        count_line += oss_meta.oss_line_count if oss_meta.oss_line_count else 0
        count_file += oss_meta.oss_file_count if oss_meta.oss_file_count else 0
        count_commit += oss_meta.oss_commit_count if oss_meta.oss_commit_count else 0
        count_developer += oss_meta.oss_developer_count if oss_meta.oss_developer_count else 0
    extra_info.update({'loc': count_line})
    extra_info.update({'foc': count_file})
    extra_info.update({'coc': count_commit})
    extra_info.update({'doc': count_developer})
    return render(request, 'overview.html', extra_info)