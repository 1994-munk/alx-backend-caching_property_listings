# properties/utils.py

# 🧩 Import necessary modules
from django.core.cache import cache
from .models import Property


def get_all_properties():
    """
    Retrieve all Property objects from cache if available,
    otherwise fetch from DB and cache the result for 1 hour.
    """
    # 🧠 Try to get from cache
    properties = cache.get('all_properties')

    if not properties:
        # 🚀 Cache miss: fetch from DB
        properties = list(Property.objects.all().values())
        # 💾 Store in Redis cache for 1 hour (3600 seconds)
        cache.set('all_properties', properties, timeout=3600)

    # ✅ Return cached or freshly fetched data
    return properties
