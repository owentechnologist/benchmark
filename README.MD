to run:
1. Create a virtual environment:

```
python3 -m venv rload
```

2. Activate it:  [This step is repeated anytime you want this venv back]

```
source rload/bin/activate
```

3. Install the libraries: 
[only necesary to do this one time per environment --> unless you add libraries to the requirements.txt file]

```
pip3 install -r requirements.txt
```

4. when you are done working with this project you can deactivate the virtual environment:

```
deactivate
```

## You can use load_strings_in_batches.py to load many keys into redis

Each String key written is equal to around 100 bytes - for every 10k keys you are using roughly 10MB of RAM.

Note: that if you are writing the same keys to an Active Active Database - you will see additional memory overhead to enable the metadata for eventual consistency.  Use RedisInsight https://redis.com/redis-enterprise/redis-insight/ to look at memory usage (and also easily delete all those keys at once using bulk commands)

## you can use many_client_connections.py to create many client connections

It is difficult to overload redis enterprise with too many connections from a single client process - you may have to start this from multiple locations to gang up on the DB enough to stress it.  



