from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from agencies.permissions import PERMISSION_AGENCY_EDIT, PERMISSION_AGENCY_VIEW
from navigation.classes import Link

from .icons import (icon_projects, icon_project_edit, icon_project_delete,
    icon_project_view, icon_agency_projects, icon_project_create,
    icon_project_info_edit, icon_project_info_view, icon_project_info_delete,
    icon_project_budget_edit, icon_project_budget_view, icon_project_budget_delete,
    icon_project_details_edit, icon_project_details_view, icon_project_details_delete,
    icon_project_opportunities_edit, icon_project_opportunities_view, icon_project_opportunities_delete,
    icon_project_file_list, icon_project_file_upload)
#from .permissions import (PERMISSION_PROJECT_EDIT, PERMISSION_PROJECT_DELETE,
#    PERMISSION_PROJECT_VIEW)

link_projects = Link(text=_(u'projects'), view='project_list', icon=icon_projects)

link_project_edit = Link(text=_(u'edit'), view='project_edit', args='resolved_object.pk', icon=icon_project_edit, permissions=[PERMISSION_AGENCY_EDIT])
link_project_delete = Link(text=_(u'delete'), view='project_delete', args='resolved_object.pk', icon=icon_project_delete, permissions=[PERMISSION_AGENCY_EDIT])
link_project_view = Link(text=_(u'project'), view='project_view', args='resolved_object.pk', icon=icon_project_view, permissions=[PERMISSION_AGENCY_VIEW])
link_project_create = Link(text=_(u'create project'), view='project_create', args='resolved_object.pk', icon=icon_project_create, permissions=[PERMISSION_AGENCY_EDIT])

link_project_info_edit = Link(text=_(u'edit'), view='project_info_edit', args='resolved_object.pk', icon=icon_project_info_edit, permissions=[PERMISSION_AGENCY_EDIT])
link_project_info_delete = Link(text=_(u'delete'), view='project_info_delete', args='resolved_object.pk', icon=icon_project_info_delete, permissions=[PERMISSION_AGENCY_EDIT])
link_project_info_view = Link(text=_(u'information'), view='project_info_view', args='resolved_object.pk', icon=icon_project_info_view, permissions=[PERMISSION_AGENCY_VIEW])

link_project_budget_edit = Link(text=_(u'edit'), view='project_budget_edit', args='resolved_object.pk', icon=icon_project_budget_edit, permissions=[PERMISSION_AGENCY_EDIT])
link_project_budget_delete = Link(text=_(u'delete'), view='project_budget_delete', args='resolved_object.pk', icon=icon_project_budget_delete, permissions=[PERMISSION_AGENCY_EDIT])
link_project_budget_view = Link(text=_(u'budget'), view='project_budget_view', args='resolved_object.pk', icon=icon_project_budget_view, permissions=[PERMISSION_AGENCY_VIEW])

link_project_details_edit = Link(text=_(u'edit'), view='project_details_edit', args='resolved_object.pk', icon=icon_project_details_edit, permissions=[PERMISSION_AGENCY_EDIT])
link_project_details_delete = Link(text=_(u'delete'), view='project_details_delete', args='resolved_object.pk', icon=icon_project_details_delete, permissions=[PERMISSION_AGENCY_EDIT])
link_project_details_view = Link(text=_(u'details'), view='project_details_view', args='resolved_object.pk', icon=icon_project_details_view, permissions=[PERMISSION_AGENCY_VIEW])

link_project_opportunities_edit = Link(text=_(u'edit'), view='project_opportunities_edit', args='resolved_object.pk', icon=icon_project_opportunities_edit, permissions=[PERMISSION_AGENCY_EDIT])
link_project_opportunities_delete = Link(text=_(u'delete'), view='project_opportunities_delete', args='resolved_object.pk', icon=icon_project_opportunities_delete, permissions=[PERMISSION_AGENCY_EDIT])
link_project_opportunities_view = Link(text=_(u'opportunities'), view='project_opportunities_view', args='resolved_object.pk', icon=icon_project_opportunities_view, permissions=[PERMISSION_AGENCY_VIEW])

link_project_file_list = Link(text=_(u'files'), view='project_file_list', args='resolved_object.pk', icon=icon_project_file_list, permissions=[PERMISSION_AGENCY_VIEW])
link_project_file_upload = Link(text=_(u'upload'), view='project_file_upload', args='resolved_object.pk', icon=icon_project_file_upload, permissions=[PERMISSION_AGENCY_VIEW])

link_agency_project_list = Link(text=_(u'projects'), view='agency_project_list', args='resolved_object.pk', icon=icon_agency_projects)
#link_project_create_wizard = Link(text=_(u'create project'), view='project_create_wizard', args='resolved_object.pk', icon=icon_project_create_wizard)
