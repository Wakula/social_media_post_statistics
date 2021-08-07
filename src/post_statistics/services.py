from post_statistics import models


def create_post_statistics(*, user_id: int, post_id: int, likes_count: int):
    models.PostStatistics.objects.create(
        user_id=user_id,
        post_id=post_id,
        likes_count=likes_count,
    )
