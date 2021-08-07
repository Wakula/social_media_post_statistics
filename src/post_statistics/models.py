from django.core.validators import MinValueValidator
from django.db import models


class PostStatistics(models.Model):
    user_id = models.IntegerField(validators=[MinValueValidator(1)])
    post_id = models.IntegerField(validators=[MinValueValidator(1)])
    likes_count = models.IntegerField(validators=[MinValueValidator(1)])
    acquired_at = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.full_clean()
        super().save(force_insert, force_update, using, update_fields)
