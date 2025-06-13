from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def navigation_view(request):
    """
    View function to render the navigation page.
    """
    user = request.user
    organization = user.get_default_organization()
    return render(request, 'front/navigation.html', {
        'organization': organization
    })
