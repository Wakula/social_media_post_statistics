from django.core.exceptions import ValidationError
from post_statistics.models import PostStatistics
from typing import Iterable


def retrieve_latest_statistics_by_post(*, post_id: int) -> PostStatistics:
    try:
        return PostStatistics.objects.filter(post_id=post_id).latest('acquired_at')
    except PostStatistics.DoesNotExist:
        raise ValidationError({'post_id': 'Does not exits.'})


def list_latest_statistics_by_user(*, user_id: int) -> Iterable[PostStatistics]:
    return (
        PostStatistics.objects
            .filter(user_id=user_id)
            .distinct('post_id')
            .order_by('post_id', '-acquired_at')
    )
