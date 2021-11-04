from rest_framework import serializers


class PostStatisticsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    post_id = serializers.IntegerField()
    likes_count = serializers.IntegerField()


class PostStatisticsByPostQueryParamsSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()


class PostStatisticsByUserQueryParamsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
