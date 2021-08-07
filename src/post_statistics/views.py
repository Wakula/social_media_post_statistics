from post_statistics import selectors
from common.mixins import ApiErrorsMixin
from post_statistics import services
from post_statistics import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.viewsets import ViewSet


class PostStatisticsViewSet(ApiErrorsMixin, ViewSet):
    def create(self, request: Request) -> Response:
        input_serializer = serializers.PostStatisticsCreateInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        services.create_post_statistics(
            **input_serializer.validated_data
        )
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def latest_by_post(self, request: Request) -> Response:
        query_params_serializer = serializers.PostStatisticsByPostQueryParamsSerializer(
            data=request.query_params
        )
        query_params_serializer.is_valid(raise_exception=True)
        output_serializer = serializers.PostStatisticsOutputSerializer(
            selectors.retrieve_latest_statistics_by_post(
                **query_params_serializer.validated_data
            )
        )
        return Response(output_serializer.data)

    @action(detail=False, methods=['get'])
    def latest_by_user(self, request: Request) -> Response:
        query_params_serializer = serializers.PostStatisticsByUserQueryParamsSerializer(
            data=request.query_params
        )
        query_params_serializer.is_valid(raise_exception=True)
        output_serializer = serializers.PostStatisticsOutputSerializer(
            selectors.list_latest_statistics_by_user(
                **query_params_serializer.validated_data
            ),
            many=True,
        )
        return Response(output_serializer.data)
