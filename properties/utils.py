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

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and compute the hit ratio.
    Returns a dictionary of results.
    """
    try:
        # Connect to Redis using the 'default' Django cache
        redis_conn = get_redis_connection("default")
        
        # Get Redis info dictionary
        info = redis_conn.info()
        
        # Extract relevant metrics
        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        
        # Calculate hit ratio safely
        total = hits + misses
        hit_ratio = (hits / total) if total > 0 else 0
        
        # Log the metrics for monitoring
        logger.info(f"Redis Cache Metrics: Hits={hits}, Misses={misses}, Hit Ratio={hit_ratio:.2%}")
        
        # Return dictionary for debugging or API reporting
        return {
            "hits": hits,
            "misses": misses,
            "hit_ratio": round(hit_ratio, 4)
        }
    
    except Exception as e:
        logger.error(f"Error retrieving Redis metrics: {e}")
        return {"error": str(e)}