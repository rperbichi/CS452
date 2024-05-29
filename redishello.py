import redis
import time

# Establish a connection to the Redis database 0 at 

host = 'redis-14332.c331.us-west1-1.gce.redns.redis-cloud.com'       # Enter your redis hostname
port = 14332        # Enter your redis port
password = 'ApgvxB8gv9YxB0BbxtpLeKlpnLcb4Tip'   # Enter the password for your redis database

r = redis.Redis(host=host, port=port, password=password, db=0)

# SET hello world

r.set('hello', 'world') # True

# GET hello

world = r.get('hello')

print(world.decode()) # "world"

# SET bye "In 60 seconds, I'll self-delete" EX 60

r.set('bye', "In 60 seconds, I'll self-delete", ex=60) # True

expiring_message = r.get('bye')

print(expiring_message.decode()) # "In 60 seconds, I'll self-delete"


# Wait 60 seconds

time.sleep(60)


# GET bye

expired_message = r.get('bye')

if expired_message == None:

    print('key "bye" is not there anymore.')

else:

    print(expired_message.decode()) # "None"

# DEL hello

r.delete('hello')

ans = r.get('hello')

if ans == None:

    print('key "hello" is not there anymore.')

else:

    print(ans.decode()) # "None"  