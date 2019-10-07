from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from math import floor

class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data,
            'timestamp': floor(timezone.now().timestamp())
        })
