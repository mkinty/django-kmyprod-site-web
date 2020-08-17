from django.urls import reverse_lazy
NAV_KMYPROD = 'Accueil'
NAV_SERVICES = 'Services'
NAV_PROJET = 'Projets'
NAV_POSTS = 'Blog'
NAV_EDUCA ='Formations'
NAV_INSTRUCTORS = 'Professeurs'
NAV_INFO = 'Contact'



NAV_ITEMS =(
    (NAV_KMYPROD, reverse_lazy('kmyprod')),
    (NAV_SERVICES, reverse_lazy('services')),
    (NAV_PROJET, reverse_lazy('projets')),
    (NAV_POSTS, reverse_lazy('blog:post_list')),
    (NAV_EDUCA, reverse_lazy('course_list')),
    (NAV_INSTRUCTORS, reverse_lazy('instructors')),
    (NAV_INFO, reverse_lazy('contact')),
)

def navigation_items(selected_item):
    items = []
    for name, url in NAV_ITEMS:
        items.append({
            'name': name,
            'url': url,
            'active': True if selected_item == name else False
        })
    return items
