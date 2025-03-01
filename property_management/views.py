from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Property
from .serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()  # Get the property instance
            serializer = self.get_serializer(instance, data=request.data, partial=True)  # Allow partial updates
            serializer.is_valid(raise_exception=True)  # Validate the data
            self.perform_update(serializer)  # Save the updated instance
            return Response(serializer.data)  # Return the updated data
        except Property.DoesNotExist:
            return Response({"error": "Property not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()  # Get the property instance
            instance.delete()  # Delete the instance
            return Response(status=status.HTTP_204_NO_CONTENT)  # Return 204 No Content
        except Property.DoesNotExist:
            return Response({"error": "Property not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)