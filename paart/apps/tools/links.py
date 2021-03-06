from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.classes import Link

from .icons import (icon_tools_profile_create, icon_tools_profile_delete, 
    icon_tools_profile_edit, icon_tools_profile_view, icon_agency_tools_profile)
from .permissions import (PERMISSION_TOOLS_PROFILE_EDIT, PERMISSION_TOOLS_PROFILE_DELETE,
    PERMISSION_TOOLS_PROFILE_VIEW)

link_tools_profile_create = Link(text=_(u'add tool profile'), view='tools_profile_create', args='agency.pk', icon=icon_tools_profile_create)#, permissions=[PERMISSION_TOOLS_PROFILE_EDIT])
link_tools_profile_delete = Link(text=_(u'delete'), view='tools_profile_delete', args='resolved_object.pk', icon=icon_tools_profile_delete)#, permissions=[PERMISSION_TOOLS_PROFILE_DELETE])
link_tools_profile_edit = Link(text=_(u'edit'), view='tools_profile_edit', args='resolved_object.pk', icon=icon_tools_profile_edit)#, permissions=[PERMISSION_TOOLS_PROFILE_EDIT])
link_tools_profile_view = Link(text=_(u'details'), view='tools_profile_view', args='resolved_object.pk', icon=icon_tools_profile_view)#, permissions=[PERMISSION_TOOLS_PROFILE_VIEW])
link_agency_tools_profile_list = Link(text=_(u'tools'), view='agency_tools_profile_list', args='resolved_object.pk', icon=icon_agency_tools_profile)
