from django.shortcuts import render,redirect
from django.http import HttpResponse
from model.user import *
from model.oss import *
from model.community import *


def searchoss(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    extra_info = dict()
    uid = request.session['user_id']
    community = OsslibCommunity.objects.filter(user_id=int(uid))
    extra_info.__setitem__('community', community)
    community_list = OsslibCommunityList.objects.filter(community_id__in=community)
    extra_info.__setitem__('community_list', community_list)
    if request.method == "POST":
        key = request.POST.get('serachoss')
        oss_id = OsslibTopic.objects.filter(topic=key)

        oss_info_all = []
        for per_oss_id in oss_id:
            oss_info = OsslibMeta.objects.filter(community_id=per_oss_id.oss_id)
            if oss_info:
                oss_info_all.append(oss_info[0])
        extra_info.__setitem__('oss', oss_info_all)
        print(extra_info)
        return render(request, 'addoss.html', extra_info)
    return render(request, 'addoss.html', extra_info)

def addtolist(request):
    oss_id = request.POST.get('oss_id')
    oss_name = request.POST.get('oss_name')
    community_id = request.POST.get('community_id')
    oss_community_list = OsslibCommunityList()
    oss_community_list.community_id = community_id
    oss_community_list.oss_id = oss_id
    oss_community_list.oss_name = oss_name
    oss_community_list.save()
    return HttpResponse('1', content_type='application/text')