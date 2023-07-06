from django.http import JsonResponse


class PostNotFoundException(Exception):
    # this should not work
    raise JsonResponse({"code":400,"details":"Post not found"})