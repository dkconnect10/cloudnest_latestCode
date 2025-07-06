from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..serializers import HospitalCreateSerializer, HospitalResponseSerializer

def hospital_create_schema():
    return swagger_auto_schema(
        request_body=HospitalCreateSerializer,
        operation_description="Create a hospital (Address ID and License ID required in context)",
        responses={
            201: openapi.Response("Hospital created successfully", HospitalResponseSerializer),
            400: "Bad Request - Missing or Invalid Data",
            401: "Unauthorized"
        }
    )
