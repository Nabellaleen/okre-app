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
