from __future__ import absolute_import

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse, resolve
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from acls.models import AccessEntry
from agencies.models import Agency
from permissions.models import Permission

#from .forms import ToolsProfileForm_create, ToolsProfileForm_edit, ToolsProfileForm_detail
#from .icons import icon_tools_profile_delete
from .models import AgencySoftware
from .permissions import (PERMISSION_AGENCY_SOFTWARE_CREATE, PERMISSION_AGENCY_SOFTWARE_DELETE,
    PERMISSION_AGENCY_SOFTWARE_EDIT, PERMISSION_AGENCY_SOFTWARE_VIEW)


def agency_software_list(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)
    pre_object_list = AgencySoftware.objects.filter(agency=agency)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_SOFTWARE_VIEW])
    except PermissionDenied:
        # If user doesn't have global permission, get a list of document
        # for which he/she does hace access use it to filter the
        # provided object_list
        final_object_list = AccessEntry.objects.filter_objects_by_access(PERMISSION_AGENCY_SOFTWARE_VIEW, request.user, pre_object_list, related='agency')
    else:
        final_object_list = pre_object_list

    context = {
        'object_list': final_object_list,
        'title': _(u'software products of: %s') % agency,
        'hide_object': True,
        'object': agency,
        'agency': agency,
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))

'''
def tools_profile_edit(request, tools_profile_pk):
    tools_profile = get_object_or_404(ToolsProfile, pk=tools_profile_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_TOOLS_PROFILE_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_TOOLS_PROFILE_EDIT, request.user, document)

    if request.method == 'POST':
        form = ToolsProfileForm_edit(request.POST, instance=tools_profile)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'ToolsProfile "%s" edited successfully.') % tools_profile)

            return HttpResponseRedirect(tools_profile.get_absolute_url())
    else:
        form = ToolsProfileForm_edit(instance=tools_profile)

    return render_to_response('generic_form.html', {
        'form': form,
        'tools_profile': tools_profile,
        'object': tools_profile,
        'agency': tools_profile.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'tools_profile'},
        ],
    }, context_instance=RequestContext(request))


def tools_profile_delete(request, tools_profile_pk):
    tools_profile = get_object_or_404(ToolsProfile, pk=tools_profile_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_TOOLS_PROFILE_DELETE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_TOOLS_PROFILE_DELETE, request.user, folder)

    post_action_redirect = reverse('agency_tools_profile_list', args=[tools_profile.agency.pk])

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            tools_profile.delete()
            messages.success(request, _(u'ToolsProfile: %s deleted successfully.') % tools_profile)
        except Exception, e:
            messages.error(request, _(u'ToolsProfile: %(tools_profile)s delete error: %(error)s') % {
                'tools_profile': tools_profile, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'object_name': _(u'tools_profile'),
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you with to delete the tools_profile: %s?') % tools_profile,
        'form_icon': icon_tools_profile_delete,
        'tools_profile': tools_profile,
        'agency': tools_profile.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'tools_profile'},
        ],
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


def tools_profile_view(request, tools_profile_pk):
    tools_profile = get_object_or_404(ToolsProfile, pk=tools_profile_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_TOOLS_PROFILE_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_TOOLS_PROFILE_VIEW, request.user, tools_profile)

    form = ToolsProfileForm_detail(instance=tools_profile)

    return render_to_response('generic_detail.html', {
        'form': form,
        'tools_profile': tools_profile,
        'object': tools_profile,
        'agency': tools_profile.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'tools_profile'},
        ],
    }, context_instance=RequestContext(request))


def tools_profile_create(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_TOOLS_PROFILE_CREATE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_TOOLS_PROFILE_CREATE, request.user, agency)

    if request.method == 'POST':
        form = ToolsProfileForm_create(request.POST)
        if form.is_valid():
            tools_profile = form.save(commit=False)
            tools_profile.agency = agency
            tools_profile.save()
            form.save_m2m()
            messages.success(request, _(u'ToolsProfile "%s" edited successfully.') % tools_profile)

            return HttpResponseRedirect(reverse('agency_tools_profile_list', args=[agency.pk]))
    else:
        form = ToolsProfileForm_create()

    return render_to_response('generic_form.html', {
        'form': form,
        'agency': agency,
        'navigation_object_list': [
            {'object': 'agency'},
        ],
        'title': _(u'Add tools profile for agency: %s') % agency,
    }, context_instance=RequestContext(request))
'''
