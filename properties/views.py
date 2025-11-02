# properties/views.py

# 🧩 Import necessary modules
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from .models import Property


@csrf_exempt
@cache_page(60 * 15)  # Cache this view for 15 minutes (900 seconds)
def property_list(request):
    """
    View to return all properties as JSON.
    Cached in Redis for 15 minutes.
    """
    # 🏡 Retrieve all property records
    properties = Property.objects.all().values()

    # 🧱 Convert the queryset to a list of dictionaries
    data = list(properties)

    # 💬 Return the response wrapped inside a 'data' key
    return JsonResponse({"data": data})
