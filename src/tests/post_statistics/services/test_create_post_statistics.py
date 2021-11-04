from django.core.exceptions import ValidationError
import pytest

from post_statistics.models import PostStatistics
from post_statistics.services import create_post_statistics

pytestmark = pytest.mark.django_db # noqa


def test_raises_validation_error_when_invalid_likes_count_passed(faker):
    with pytest.raises(ValidationError):
        create_post_statistics(
            user_id=faker.pyint(min_value=1),
            post_id=faker.pyint(min_value=1),
            likes_count=faker.pyint(min_value=-100, max_value=-1)
        )


def test_creates_post_statistics_when_valid_data_passed(faker):
    create_post_statistics(
        user_id=faker.pyint(min_value=1),
        post_id=faker.pyint(min_value=1),
        likes_count=faker.pyint(min_value=1)
    )

    assert PostStatistics.objects.exists()
