from django.conf import settings
from urllib.parse import urljoin, urlparse
from civictechprojects.models import Event
from civictechprojects.caching.cache import ProjectCache, GroupCache
from common.helpers.constants import FrontEndSection
from common.helpers.front_end import section_url
from common.helpers.redirectors import RedirectTo
from common.helpers.request_helpers import url_params


def about_project_preload(context, request):
    context = default_preload(context, request)
    query_args = url_params(request)
    project_id = query_args['id']
    project_json = ProjectCache.get(project_id)
    if project_json is not None:
        context['title'] = project_json['project_name'] + ' | DemocracyLab'
        context['description'] = project_json['project_short_description'] or project_json['project_description'][:300]
        if 'project_thumbnail' in project_json:
            context['og_image'] = project_json['project_thumbnail']['publicUrl']
    else:
        print('Failed to preload project info, no cache entry found: ' + project_id)
    return context


def about_event_preload(context, request):
    context = default_preload(context, request)
    query_args = url_params(request)
    event_id = query_args['id']
    event = Event.get_by_id_or_slug(event_id)
    event_json = event.hydrate_to_json()
    if event_json is not None:
        context['title'] = event_json['event_name'] + ' | DemocracyLab'
        context['description'] = event_json['event_short_description']
        if 'event_thumbnail' in event_json:
            context['og_image'] = event_json['event_thumbnail']['publicUrl']
        slug_or_id = event.event_slug or event.id
        context['canonical_url'] = section_url(FrontEndSection.AboutEvent,  {'id': slug_or_id})
    else:
        print('Failed to preload event info, no cache entry found: ' + event_id)
    return context


def about_group_preload(context, request):
    context = default_preload(context, request)
    query_args = url_params(request)
    group_id = query_args['id']
    group_json = GroupCache.get(group_id)
    if group_json is not None:
        context['title'] = group_json['group_name'] + ' | DemocracyLab'
        context['description'] = group_json['group_short_description']
        if 'group_thumbnail' in group_json:
            context['og_image'] = group_json['group_thumbnail']['publicUrl']
    else:
        print('Failed to preload group info, no cache entry found: ' + group_id)
    return context


def companies_preload(context, request):
    context = default_preload(context, request)
    context['title'] = 'DemocracyLab | Corporate Engagement'
    context['description'] = 'Do well by doing good! Engage employees at custom events to build culture and spark innovation. Differentiate your brand by sponsoring our public hackathons.'
    return context


def about_us_preload(context, request):
    context = default_preload(context, request)
    context['title'] = 'DemocracyLab | About'
    context['description'] = 'Learn About democracyLab, the nonprofit connecting skilled individuals to tech-for-good projects.'
    return context


def donate_preload(context, request):
    context = default_preload(context, request)
    context['title'] = 'Donate | DemocracyLab'
    context['description'] = 'Your donation empowers people who use technology for public good by connecting tech-for-good projects to skilled volunteers and socially responsible companies.'
    return context


def edit_profile_preload(context, request):
    context = default_preload(context, request)
    context['title'] = 'Update User Profile | DemocracyLab'
    context['description'] = 'Update User Profile page'
    return context


def create_event_preload(context, request):
    context = default_preload(context, request)
    context['title'] = 'Create an Event | DemocracyLab'
    context['description'] = 'Create event page'
    return context


def my_projects_preload(context, request):
    context = default_preload(context, request)
    context['title'] = 'My Projects | DemocracyLab'
    context['description'] = 'My Projects page'
    return context


def my_groups_preload(context, request):
    context = default_preload(context, request)
    context['title'] = 'My Groups | DemocracyLab'
    context['description'] = 'My Groups page'
    return context


def my_events_preload(context, request):
    context = default_preload(context, request)
    context['title'] = 'My Events | DemocracyLab'
    context['description'] = 'My Events page'
    return context


def videos_preload(context, request):
    context = default_preload(context, request)
    if settings.VIDEO_PAGES:
        query_args = url_params(request)
        video_id = query_args['id']
        if video_id in settings.VIDEO_PAGES:
            video_json = settings.VIDEO_PAGES[video_id]
            context['YOUTUBE_VIDEO_URL'] = video_json['video_url']
            if 'video_description' in video_json:
                context['description'] = video_json['video_description']
            if 'video_thumbnail' in video_json:
                context['og_image'] = video_json['video_thumbnail']
        else:
            print('Redirecting invalid video id: ' + video_id)
            raise RedirectTo(section_url(FrontEndSection.VideoOverview, {'id': 'overview'}))

    return context


def default_preload(context, request):
    context['title'] = 'DemocracyLab'
    context['description'] = 'Everyone has something to contribute to the technical solutions society needs. ' \
                             'Volunteer today to connect with other professionals volunteering their time.'
    context['og_type'] = 'website'
    context['og_image'] = settings.STATIC_CDN_URL + '/img/Democracylab_is_a_global_volunteer_tech_for_good_nonprofit.png'
    url = settings.PROTOCOL_DOMAIN + request.get_full_path()
    # Remove parameters for canonical urls by default
    context['canonical_url'] = urljoin(url, urlparse(url).path)
    return context


preload_urls = [
    {'section': FrontEndSection.AboutProject.value, 'handler': about_project_preload},
    {'section': FrontEndSection.AboutEvent.value, 'handler': about_event_preload},
    {'section': FrontEndSection.EditProfile.value, 'handler': edit_profile_preload},
    {'section': FrontEndSection.AboutUs.value, 'handler': about_us_preload},
    {'section': FrontEndSection.CreateEvent.value, 'handler': create_event_preload},
    {'section': FrontEndSection.MyProjects.value, 'handler': my_projects_preload},
    {'section': FrontEndSection.MyGroups.value, 'handler': my_groups_preload},
    {'section': FrontEndSection.MyEvents.value, 'handler': my_events_preload},
    {'section': FrontEndSection.Donate.value, 'handler': donate_preload},
    {'section': FrontEndSection.AboutGroup.value, 'handler': about_group_preload},
    {'section': FrontEndSection.Companies.value, 'handler': companies_preload},
    {'section': FrontEndSection.VideoOverview.value, 'handler': videos_preload}
]


def context_preload(section, request, context):
    handler = next((preload_url['handler'] for preload_url in preload_urls if preload_url['section'] == section), default_preload)
    return handler(context, request)

