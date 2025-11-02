# properties/views.py

# 🧩 Import necessary modules
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from .models import Property



@csrf_exempt
@cache_page(60 * 15)  # Cache the entire view for 15 minutes
def property_list(request):
    """
    View to return all properties as JSON.
    Uses low-level Redis cache for queryset and view cache for response.
    """
    # 🧠 Fetch properties using the cached helper
    properties = get_all_properties()

    # 💬 Return data in JSON format
    return JsonResponse({"data": properties})
