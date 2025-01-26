import time

import furl
import redis

from ..utils import (
    REDIS_HOST,
    REDIS_PORT,
    MAX_CALLS,
    TIME_FRAME,
)


class RateLimiter:
    def __init__(self, scheme=None, host=REDIS_HOST, port=REDIS_PORT,
                 max_calls=MAX_CALLS, time_frame=TIME_FRAME):
        if scheme:
            host = str(furl.furl(scheme).host)
            port = str(furl.furl(scheme).port)
        self.redis_client = redis.StrictRedis(host=host, port=port,
                                              decode_responses=True)
        self.max_calls = max_calls
        self.time_frame = time_frame
        self.lua_script = """
        local key = KEYS[1]
        local current_time = tonumber(ARGV[1])
        local time_frame = tonumber(ARGV[2])
        local max_calls = tonumber(ARGV[3])

        -- Remove old timestamps
        redis.call('ZREMRANGEBYSCORE', key, 0, current_time - time_frame)

        -- Get the current count of timestamps
        local count = redis.call('ZCARD', key)

        if count < max_calls then
            -- Add the new timestamp
            redis.call('ZADD', key, current_time, current_time)
            redis.call('EXPIRE', key, time_frame)
            return 1 -- Allowed
        else
            return 0 -- Denied
        end
        """
        self.script_sha = self.redis_client.script_load(self.lua_script)

    def is_allowed(self, user_id):
        current_time = int(time.time() * 1000)
        key = f'rate_limiter:{user_id}'
        result = self.redis_client.evalsha(self.script_sha, 1, key,
                                           current_time,
                                           self.time_frame * 1000,
                                           self.max_calls)
        return result == 1
