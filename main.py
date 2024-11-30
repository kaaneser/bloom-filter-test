from bloom.bloom_filter import BloomFilter
from cache.redis_cache import RedisCache

# Initialize Bloom Filter and Redis
bloom_filter = BloomFilter()
cache = RedisCache()

def query_data(key):
    if bloom_filter.check(key):
        cached_data = cache.get(key)

        if cached_data:
            print(f"Cache hit: {cached_data.decode()}")
            return cached_data.decode()
        else:
            print("Cache miss, querying db...")
            data = f"Fetched data for {key}"
            cache.set(key, data)
            bloom_filter.add(key)
            return data
        
    else:
        print("Not found in Bloom Filter, querying db...")
        data = f"Fetched data for {key}"
        cache.set(key, data)
        bloom_filter.add(key)
        return data

# Case 1: Query for an item that actually exists    
print("First query (should be a cache miss and DB query):")
print(query_data("user:123")) # Real user key

# Case 2: Repeat the same query for the same item (Cache hit)
print("\nSecond query (should be a cache hit):")
print(query_data("user:123")) # Should get it from Redis

# Case 3: Triggering the false positive condition
bloom_filter.add("user:999") # Test data, for triggering false positive cond.
print("\nQuery with a false positive (user:999):")
print(query_data("user:999"))
