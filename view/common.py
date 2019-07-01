from model.oss import *
from model.community import *
from model.user import *


def get_nav_list(uid):
    extra_info = dict()
    community = OsslibCommunity.objects.filter(user_id=int(uid))
    community_list = OsslibCommunityList.objects.filter(community_id__in=community)
    extra_info.__setitem__('community', community)
    extra_info.__setitem__('community_list', community_list)
    user = OsslibUser.objects.get(id=uid)
    extra_info.__setitem__('user', user)
    return extra_info
