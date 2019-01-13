from django.http import JsonResponse

from rest_framework import status


def bad_request(request, exception, *args, **kwargs):
    """
    Generic 400 error handler.
    """
    data = {
        'status': status.HTTP_400_BAD_REQUEST,
        'error': 'Bad Request (400)'
    }
    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)


def permission_denied(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """
    data = {
        'status': status.HTTP_403_FORBIDDEN,
        'error': 'Permission Denied (403)'
    }
    return JsonResponse(data, status=status.HTTP_403_FORBIDDEN)


def page_not_found(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """
    data = {
        'status': status.HTTP_404_NOT_FOUND,
        'error': 'Page Not Found (404)'
    }
    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)


def server_error(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """
    data = {
        'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
        'error': 'Server Error (500)'
    }
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)