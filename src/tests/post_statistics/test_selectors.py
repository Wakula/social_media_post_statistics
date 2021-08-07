from django.test import TestCase
from django.core.exceptions import ValidationError
from post_statistics.models import PostStatistics
from post_statistics.selectors import retrieve_latest_statistics_by_post
from post_statistics.services import create_post_statistics


class TestRetrieveLatestStatisticsByPost(TestCase):
    def test_non_existent_post_id_statistics(self):
        non_existent_post_id = 1

        with self.assertRaises(ValidationError):
            retrieve_latest_statistics_by_post(
                post_id=non_existent_post_id
            )

    def test_multiple_post_id_statistics(self):
        post_id = 1
        user_id = 1
        PostStatistics.objects.create(
            post_id=post_id,
            user_id=user_id,
            likes_count=13,
        )
        latest_post = PostStatistics.objects.create(
            post_id=post_id,
            user_id=user_id,
            likes_count=11,
        )

        result = retrieve_latest_statistics_by_post(post_id=post_id)

        self.assertEqual(latest_post, result)


class TestCreatePostStatistics(TestCase):
    def test_invalid_data_passed(self):
        with self.assertRaises(ValidationError):
            create_post_statistics(
                user_id=1,
                post_id=1,
                likes_count=-11
            )

    def test_successful_creation(self):
        create_post_statistics(
            user_id=1,
            post_id=1,
            likes_count=1
        )

        self.assertTrue(PostStatistics.objects.exists())
