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

from django.db import models

class Objective(models.Model):
    """
    Model to represent objectives.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    team = models.ForeignKey(
        'organization.Team',
        on_delete=models.CASCADE,
        related_name='objectives',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_advancement(self):
        """
        Calculate the advancement of the objective based on its key results.
        Returns a dictionary with the total target and current values,
        and the advancement percentage.
        """
        key_results = self.key_results.all()
        total_target = sum(kr.target_value for kr in key_results)
        total_current = sum(kr.current_value for kr in key_results)
        if total_target > 0:
            advancement = round((total_current / total_target) * 100, 2)
        else:
            advancement = 0
        return {
            "total_target": total_target,
            "total_current": total_current,
            "advancement": advancement,
        }


class KeyResult(models.Model):
    """
    Model to represent key results associated with objectives.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    target_value = models.FloatField()
    current_value = models.FloatField()
    objective = models.ForeignKey(
        Objective,
        on_delete=models.CASCADE,
        related_name='key_results',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.current_value}/{self.target_value})"
    
    def get_min_max_values(self):
        """
        Get the minimum and maximum values for the key result.
        Returns a tuple of (min_value, max_value).
        """
        min_value = min(self.current_value, self.target_value)
        max_value = max(self.current_value, self.target_value)
        return (min_value, max_value)
