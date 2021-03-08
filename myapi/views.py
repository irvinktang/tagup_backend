from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from django.db import transaction
from .serializers import RecordSerializer
from .models import Record
from .utils import getUnixTime


class GetAllRecords(ListAPIView):
    """
    View for retrieving records
    """

    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class GetRecord(RetrieveAPIView):
    """
    View to read or update a specific record
    """

    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class CreateRecord(CreateAPIView):
    """
    View for creating records
    """

    serializer_class = RecordSerializer

    @transaction.atomic
    def create(self, request):
        time_now = getUnixTime()
        record = Record()
        record.creationDate = time_now
        record.lastModificationDate = time_now
        serializer = self.serializer_class(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModifyRecord(UpdateAPIView):
    """
    View for modifiying records
    """

    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    @transaction.atomic
    def patch(self, request, pk):
        record = self.get_object()
        record.lastModificationDate = getUnixTime()
        serializer = self.serializer_class(
            record, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveRecord(DestroyAPIView):
    """
    View for removing records
    """

    queryset = Record.objects.all()

    @transaction.atomic
    def delete(self, request, pk):
        record = self.get_object()
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
