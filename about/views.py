from django.shortcuts import render

from navigation import navigation

# Create your views here.
def kmyprod_detail(request):
        context = {
            'navigation_items': navigation.navigation_items(navigation.NAV_KMYPROD),

        }
        return render(request, 'about/kmyprod/detail.html', context)


def services_detail(request):
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_SERVICES),

    }
    return render(request, 'about/services/detail.html', context)


def instructors_detail(request):
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_INSTRUCTORS),

    }
    return render(request, 'about/instructors/detail.html', context)


def contact_detail(request):
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_INFO),

    }
    return render(request, 'about/contact/detail.html', context)


def projets_detail(request):
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_PROJET),

    }
    return render(request, 'about/projets/detail.html', context)
