from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 10

    # This allows us to pass page_size and bypass the default page size
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(
            {
                "results": data,
                "meta": {
                    "total_count": self.page.paginator.count,
                    "total_pages": self.page.paginator.num_pages,
                    "current_page": self.page.number,
                    "page_size": self.get_page_size(self.request),
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
            }
        )
