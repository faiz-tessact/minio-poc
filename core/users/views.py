import datetime
import random

from minio import Minio

from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import (action, api_view,
                                       authentication_classes,
                                       permission_classes)
from rest_framework.response import Response

URL = 'minio:9000'
access_key = "qrp4dL7gLbMlM0U9oGQV"
access_secret = "vh0NGsy8NC2FjoNb8XwcJwddwjEJvhK4GQZskkdg"
client = Minio(URL, access_key=access_key, secret_key=access_secret, secure=False)


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def list_buckets(request):
    buckets = client.list_buckets()
    data = []
    for bucket in buckets:
        data.append(bucket.name)
    return Response(data=data, status=status.HTTP_200_OK)




@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def list_objects(request):
    prefix = request.query_params.get("prefix", None)
    bucket = request.query_params.get("bucket", None)
    data = []
    objects = client.list_objects(bucket, prefix=prefix)
    for obj in objects:
        data.append(obj.object_name)
    return Response(data=data, status=status.HTTP_200_OK)
