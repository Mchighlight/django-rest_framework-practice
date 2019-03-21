from rest_framework import pagination

class StandardAPIPagination(pagination.LimitOffsetPagination):
    #page_size = 5
    max_limit = 10
    default_limit = 10
    limit_query_param = 'page_size'
    #max_page_size = 10