from __future__ import absolute_import

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse, resolve
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from agencies.models import Agency
from agencies.permissions import PERMISSION_AGENCY_EDIT, PERMISSION_AGENCY_VIEW
from permissions.models import Permission

from .forms import (ProjectForm_edit, ProjectForm_view, ProjectForm_create,
    ProjectInfoForm_view, ProjectInfoForm_edit, ProjectInfoForm_create)
from .icons import icon_project_delete, icon_project_info_delete
from .models import Project, ProjectInfo
from .permissions import (PERMISSION_PROJECT_EDIT, PERMISSION_PROJECT_DELETE,
    PERMISSION_PROJECT_VIEW, PERMISSION_PROJECT_CREATE)
from .wizards import ProjectCreateWizard


def agency_project_list(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)
    pre_object_list = agency.project_set.all()

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_VIEW])
    except PermissionDenied:
        # If user doesn't have global permission, get a list of document
        # for which he/she does hace access use it to filter the
        # provided object_list
        final_object_list = AccessEntry.objects.filter_objects_by_access(PERMISSION_PROJECT_VIEW, request.user, pre_object_list)
    else:
        final_object_list = pre_object_list

    context = {
        'object_list': final_object_list,
        'title': _(u'projects'),
        #'hide_object': True,
        'object': agency,
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))


def project_edit(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project.agency)

    if request.method == 'POST':
        form = ProjectForm_edit(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Project "%s" edited successfully.') % project)

            return HttpResponseRedirect(project.get_absolute_url())
    else:
        form = ProjectForm_edit(instance=project)

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project,
        'title': _(u'edit project: %s') % project,
        'agency': project.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }, context_instance=RequestContext(request))


def project_delete(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project.agency)

    post_action_redirect = reverse('agency_project_list', args=[project.agency.pk])

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            project.delete()
            messages.success(request, _(u'Project: %s deleted successfully.') % project)
        except Exception, e:
            messages.error(request, _(u'Project: %(project)s delete error: %(error)s') % {
                'project': project, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'object_name': _(u'project'),
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you with to delete the project: %s?') % project,
        'form_icon': icon_project_delete,
        'project': project,
        'agency': project.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


def project_view(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_VIEW, request.user, project.agency)

    form = ProjectForm_view(instance=project)

    return render_to_response('generic_detail.html', {
        'form': form,
        'agency': project.agency,
        'project': project,
        'title': _(u'project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }, context_instance=RequestContext(request))


def project_create(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, agency)

    if request.method == 'POST':
        form = ProjectForm_create(data=request.POST, initial={'agency': agency})
        if form.is_valid():
            project = form.save(commit=False)
            project.agency=agency
            project.save()
            messages.success(request, _(u'Project "%s" saved successfully.') % project)

            return HttpResponseRedirect(project.get_absolute_url())
    else:
        form = ProjectForm_create(initial={'agency': agency})

    return render_to_response('generic_form.html', {
        'form': form,
        'object': agency,
        'title': _(u'create project for agency: %s') % agency,
    }, context_instance=RequestContext(request))


"""
def project_create_wizard(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_CREATE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_CREATE, request.user, agency)

    wizard = ProjectCreateWizard.as_view(
        form_list=[ProjectForm_step1, ProjectForm_step2, ProjectForm_step3, ProjectForm_step4],
        step_titles=[
            _(u'General information'),
            _(u'Budget'),
            _(u'Equipment'),
            _(u'Timeframe'),
        ],
        view_extra_context={
            'object': agency,
        },
        agency=agency,
        model=Project
    )
    return wizard(request)
"""


def project_info_view(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_VIEW, request.user, project)

    try:
        project_info = project.projectinfo
    except ProjectInfo.DoesNotExist:
        return HttpResponseRedirect(reverse('project_info_create', args=[project.pk]))
    else:
        form = ProjectInfoForm_view(instance=project.projectinfo)

    return render_to_response('generic_detail.html', {
        'form': form,
        'agency': project.agency,
        'project': project,
        'project_info': project_info,
        'title': _(u'information for project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_info'},
        ],
    }, context_instance=RequestContext(request))


def project_info_edit(request, project_info_pk):
    project_info = get_object_or_404(ProjectInfo, pk=project_info_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project_info.project.agency)

    if request.method == 'POST':
        form = ProjectInfoForm_edit(request.POST, instance=project_info)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Information for project "%s" edited successfully.') % project_info.project)

            return HttpResponseRedirect(project_info.get_absolute_url())
    else:
        form = ProjectInfoForm_edit(instance=project_info)

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project_info.project,
        'project_info': project_info,
        'agency': project_info.project.agency,
        'title': _('edit information for project: %s') % project_info.project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_info'},
        ],
    }, context_instance=RequestContext(request))


def project_info_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project.agency)

    if request.method == 'POST':
        form = ProjectInfoForm_create(request.POST, initial={'project': project})
        if form.is_valid():
            project_info = form.save(commit=False)
            project_info.project = project
            project_info.save()
            messages.success(request, _(u'Details for project "%s" saved successfully.') % project)

            return HttpResponseRedirect(project.get_absolute_url())
    else:
        form = ProjectInfoForm_create(initial={'project': project})

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project,
        'agency': project.agency,
        'title': _(u'enter information for project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }, context_instance=RequestContext(request))


def project_info_delete(request, project_info_pk):
    project_info = get_object_or_404(ProjectInfo, pk=project_info_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project_info.project.agency)

    post_action_redirect = project_info.project.get_absolute_url()

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            project_info.delete()
            messages.success(request, _(u'Information for project: %s, deleted successfully.') % project_info.project)
        except Exception, e:
            messages.error(request, _(u'Information for project: %(project)s delete error: %(error)s') % {
                'project': project_info.project, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you with to delete the information for project: %s?') % project_info.project,
        'form_icon': icon_project_info_delete,
        'project': project_info.project,
        'project_info': project_info,
        'agency': project_info.project.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_info'},
        ],
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))
