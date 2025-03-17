from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Lease
from .serializers import LeaseSerializer

class LeaseList(APIView):
    def get(self, request):
        leases = Lease.objects.all()
        serializer = LeaseSerializer(leases, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LeaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaseDetail(APIView):
    def get_object(self, pk):
        try:
            return Lease.objects.get(pk=pk)
        except Lease.DoesNotExist:
            return None

    def get(self, request, pk):
        lease = self.get_object(pk)
        if lease:
            serializer = LeaseSerializer(lease)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        lease = self.get_object(pk)
        if lease:
            serializer = LeaseSerializer(lease, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        lease = self.get_object(pk)
        if lease:
            lease.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)