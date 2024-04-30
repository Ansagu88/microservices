from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    """
    Custom pagination class for small sets of data.

    This pagination class is used to paginate small sets of data in the wishlist app.
    It sets the page query parameter to 'p', the default page size to 6, and the
    page size query parameter to 'page_size'. The maximum page size is also set to 6.
    """
    page_query_param = 'p'
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 6

class MediumSetPagination(PageNumberPagination):
    """
    Custom pagination class for medium-sized sets of data.

    This pagination class is used to paginate medium-sized sets of data in the wishlist app.
    It sets the page query parameter to 'p', the default page size to 9, and the maximum page size to 9.
    """

    page_query_param = 'p'
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 9

class LargeSetPagination(PageNumberPagination):
    """
    Custom pagination class for handling large sets of data.

    Attributes:
        page_query_param (str): The query parameter name for specifying the page number.
        page_size (int): The default number of items to include on a page.
        page_size_query_param (str): The query parameter name for specifying the page size.
        max_page_size (int): The maximum number of items allowed on a page.

    """
    page_query_param = 'p'
    page_size = 14
    page_size_query_param = 'page_size'
    max_page_size = 14