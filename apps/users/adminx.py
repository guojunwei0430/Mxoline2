# encoding: utf-8
from django.contrib.auth.models import Group, Permission

from operation.models import CourseComments, UserFavorite, UserMessage, UserCourse, UserAsk
from organization.models import CityDict, Teacher, CourseOrg
from xadmin.layout import Main, Row, Side
from xadmin.models import Log
from xadmin.plugins.auth import UserAdmin
from django.utils.translation import ugettext as _

__author__ = 'mtianyan'
__date__ = '2018/1/9 0009 08:02'
import xadmin
from xadmin import views
from courses.models import Course, Lesson, Video, CourseResource
from .models import EmailVerifyRecord, Banner, UserProfile


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

class GlobalSettings(object):
    site_title = "天涯明月笙: 慕课后台管理站"
    site_footer = "mtianyan's mooc"
    menu_style = "accordion"

    def get_site_menu(self):
        return(
            {'title': '机构管理', 'menus': (
                {'title': '所在城市', 'url': self.get_model_url(CityDict, 'changelist')},
                {'title': '机构信息', 'url': self.get_model_url(CourseOrg, 'changelist')},
                {'title': '机构讲师', 'url': self.get_model_url(Teacher, 'changelist')},
            )},
        {'title': '课程管理', 'menus': (
                 {'title': '课程信息', 'url': self.get_model_url(Course, 'changelist')},
                 {'title': '章节信息', 'url': self.get_model_url(Lesson, 'changelist')},
                 {'title': '视频信息', 'url': self.get_model_url(Video, 'changelist')},
                 {'title': '课程资源', 'url': self.get_model_url(CourseResource, 'changelist')},
                 {'title': '课程评论', 'url': self.get_model_url(CourseComments, 'changelist')},
             )},

             {'title': '用户管理', 'menus': (
                 {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
                 {'title': '用户验证', 'url': self.get_model_url(EmailVerifyRecord, 'changelist')},
                 {'title': '用户课程', 'url': self.get_model_url(UserCourse, 'changelist')},
                 {'title': '用户收藏', 'url': self.get_model_url(UserFavorite, 'changelist')},
                 {'title': '用户消息', 'url': self.get_model_url(UserMessage, 'changelist')},
             )},


             {'title': '系统管理', 'menus': (
                 {'title': '用户咨询', 'url': self.get_model_url(UserAsk, 'changelist')},
                 {'title': '首页轮播', 'url': self.get_model_url(Banner, 'changelist')},
                 {'title': '用户分组', 'url': self.get_model_url(Group, 'changelist')},
                 {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
                 {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
             )},
        )


class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']

xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)