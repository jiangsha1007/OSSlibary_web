from django.shortcuts import render,redirect
from django.http import HttpResponse
from model.community import *
from model.oss import *
from view.common import *
from operator import itemgetter

def overview(request):
    extra_info = dict()
    uid = request.session['user_id']
    community = get_nav_list(uid)
    extra_info.update(community)
    cid = request.GET.get('cid')
    oss_statistic = OsslibStatistic.objects.filter(community_id=int(cid))
    count_line = 0
    count_file = 0
    count_commit = 0
    count_developer = 0
    issue_close = 0
    issue_count = 0

    oss_name = ''
    oss_score = ''
    oss_list = OsslibCommunityList.objects.filter(community_id=int(cid))
    oss_id_list = list(oss_list.values_list('oss_id', flat=True))
    oss_meta_list = OsslibMeta.objects.filter(id__in=list(oss_list.values_list('oss_id', flat=True)))
    #获取语言数量和语言分布以及评分
    lanuage_merge = dict()
    if oss_meta_list:
        for per_oss_meta in oss_meta_list:
            lanuage = per_oss_meta.oss_language
            lanuage_json = json.loads(lanuage)
            merge = dict(lanuage_json)
            for key in list(set(merge) | set(lanuage_merge)):
                if merge.get(key) and lanuage_merge.get(key):
                    lanuage_merge.update({key: lanuage_merge.get(key) + merge.get(key)})
                else:
                    lanuage_merge.update({key: merge.get(key) or lanuage_merge.get(key)})
            oss_name += per_oss_meta.oss_name+','
            oss_score += str(per_oss_meta.f1)+'-'+str(per_oss_meta.f2)+'-'+str(per_oss_meta.f3)+'-'+str(per_oss_meta.f4)+'-'+str(per_oss_meta.f5)+'-'+str(per_oss_meta.f6)+','
        oss_name = oss_name[:-1]
        oss_score = oss_score[:-1]
    lanuage_merge_sort = dict(sorted(lanuage_merge.items(), key=itemgetter(1), reverse=True))
    bar_lanuage_arr = ''
    bar_lanuage_data = ''
    y = list(lanuage_merge_sort.keys())
    for i in range(10):
        key = y[i]
        bar_lanuage_arr += y[i] + ','
        bar_lanuage_data += str(lanuage_merge_sort.get(key)) + ','
    if oss_statistic:
        count_line = oss_statistic[0].loc
        count_file = oss_statistic[0].foc
        count_commit = oss_statistic[0].coc
        count_developer = oss_statistic[0].doc
        issue_count = oss_statistic[0].issue_count
        issue_close = oss_statistic[0].issue_close_count
        pulls_count = oss_statistic[0].pull_count
        pulls_merged = oss_statistic[0].pull_merged_count
        issue_close_radio = (oss_statistic[0].issue_close_count/oss_statistic[0].issue_count)*100
        pull_merged_radio = (oss_statistic[0].pull_merged_count/oss_statistic[0].pull_count)*100
        core_developer_radio = (oss_statistic[0].core_developer_count/oss_statistic[0].doc)*100
        core_issue_radio = (oss_statistic[0].core_issue_count/oss_statistic[0].issue_count)*100
        core_pull_radio = (oss_statistic[0].core_pull_count/oss_statistic[0].pull_count)*100
        active_day_radio = (oss_statistic[0].active_days/oss_statistic[0].all_days)*100

    extra_info.update({'loc': count_line})
    extra_info.update({'foc': count_file})
    extra_info.update({'coc': count_commit})
    extra_info.update({'doc': count_developer})
    extra_info.update({'issue_count': issue_count})
    extra_info.update({'issue_close': issue_close})
    extra_info.update({'issue_open': issue_count - issue_close})
    extra_info.update({'issue_closed': round(issue_close_radio, 2)})
    extra_info.update({'pulls_count': pulls_count})
    extra_info.update({'pulls_merged': pulls_merged})
    extra_info.update({'pulls_unmerged': pulls_count - pulls_merged})
    extra_info.update({'pull_merged': round(pull_merged_radio, 2)})
    extra_info.update({'developer_core': round(core_developer_radio, 2)})
    extra_info.update({'core_issue': round(core_issue_radio, 2)})
    extra_info.update({'core_pull': round(core_pull_radio, 2)})
    extra_info.update({'active_day': round(active_day_radio, 2)})
    extra_info.update({'oss_list': oss_meta_list})
    extra_info.update({'bar_lanuage_arr': bar_lanuage_arr})
    extra_info.update({'bar_lanuage_data': bar_lanuage_data})
    extra_info.update({'oss_score': oss_score})
    extra_info.update({'oss_name': oss_name})
    return render(request, 'overview.html', extra_info)