from django.shortcuts import render
# ✨ Django imports
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse

# ✨ Import the model
from .models import Property


# 🏡 Cache this view for 15 minutes (60 sec * 15)
@cache_page(60 * 15)
def property_list(request):
    """
    View to list all properties. 
    Cached for 15 minutes in Redis for performance.
    """
    # Fetch all properties from database
    properties = Property.objects.all().values(
        "id", "title", "description", "price", "location", "created_at"
    )

    # Return the data as JSON
    return JsonResponse(list(properties), safe=False)
