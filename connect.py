import redis

def connect_redis(host='localhost', port=6379, db=0, password="TPRedisPython"):
    """
    Connect to a Redis server and return a connection object.
    """
    try:
        r = redis.StrictRedis(
            host=host,
            port=port,
            db=db,
            password=password,
            decode_responses=True # ensures utf-8 encoding
        )
        # Test connection
        r.ping()
        print("Connected to Redis!")
        return r
    except redis.ConnectionError as e:
        print(f"Could not connect to Redis: {e}")
        return None

def set_key(redis_conn, key, value, expire=None):
    """
    Set a key in Redis with optional expiry (in seconds).
    """
    try:
        redis_conn.set(name=key, value=value, ex=expire)
        print(f"Set key '{key}' to '{value}'")
    except Exception as e:
        print(f"Error setting key: {e}")

def get_key(redis_conn, key):
    """
    Get a value for a key from Redis.
    """
    try:
        value = redis_conn.get(key)
        print(f"Value for key '{key}': {value}")
        return value
    except Exception as e:
        print(f"Error getting key: {e}")
        return None

def delete_key(redis_conn, key):
    """
    Delete a key from Redis.
    """
    try:
        redis_conn.delete(key)
        print(f"Deleted key '{key}'")
    except Exception as e:
        print(f"Error deleting key: {e}")

# Example usage
if __name__ == "__main__":
    redis_conn = connect_redis()
    if redis_conn:
        set_key(redis_conn, "foo", "bar", expire=60)
        value = get_key(redis_conn, "foo")
        delete_key(redis_conn, "foo")
