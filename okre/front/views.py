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

@login_required
def objective_view(request, objective_id):
    """
    View function to render the details of a specific objective.
    """
    user = request.user
    organization = user.get_default_organization()
    
    from django.shortcuts import get_object_or_404

    objective = get_object_or_404(organization.objectives.model, id=objective_id)

    return render(request, 'front/objective.html', {
        'objective': objective,
    })
