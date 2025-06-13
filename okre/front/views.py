# Copyright (C) 2025  Florian Briand (Digital Engine)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

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
