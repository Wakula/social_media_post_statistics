from rest_framework import serializers
from post_statistics.models import PostStatistics


class PostStatisticsCreateInputSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    post_id = serializers.IntegerField()
    likes_count = serializers.IntegerField()


class PostStatisticsByPostQueryParamsSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()


class PostStatisticsByUserQueryParamsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()


class PostStatisticsOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostStatistics
        fields = ['user_id', 'post_id', 'likes_count']
