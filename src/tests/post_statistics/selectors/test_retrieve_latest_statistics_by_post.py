from django.core.exceptions import ValidationError
import pytest

from post_statistics.models import PostStatistics
from post_statistics.selectors import retrieve_latest_statistics_by_post

pytestmark = pytest.mark.django_db # noqa


def test_raises_validation_error_when_non_existent_post_id_passed(faker):
    non_existent_post_id = faker.pyint(min_value=1)

    with pytest.raises(ValidationError):
        retrieve_latest_statistics_by_post(post_id=non_existent_post_id)


def test_returns_correct_statistics_when_multiple_rows_available_for_single_post(faker):
    post_id = faker.pyint(min_value=1)

    PostStatistics.objects.create(
        post_id=post_id,
        user_id=faker.pyint(min_value=1),
        likes_count=faker.pyint(min_value=1),
    )
    expected_statistics = PostStatistics.objects.create(
        post_id=post_id,
        user_id=faker.pyint(min_value=1),
        likes_count=faker.pyint(min_value=1),
    )

    retrieved_statistics = retrieve_latest_statistics_by_post(post_id=post_id)

    assert retrieved_statistics == expected_statistics
