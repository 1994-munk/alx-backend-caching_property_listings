# properties/views.py

# 🧩 Import necessary Django modules
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

# 🧠 Import your Property model
from .models import Property


# 🏡 Create a cached view for listing all properties
@csrf_exempt
@cache_page(60 * 15)  # Cache for 15 minutes (900 seconds)
def property_list(request):
    """
    View to return all property listings as JSON.
    The response is cached in Redis for 15 minutes.
    """
    # Query all Property objects
    properties = Property.objects.all().values()

    # Convert QuerySet to a list of dictionaries
    property_list = list(properties)

    # Return JSON response
    return JsonResponse({"properties": property_list}, safe=False)
