This little utility is designed to work with redis benchmark.

It writes a specified number of sequential keys to Redis in a format that is recognized by Redis Benchmark.

This allows you to use this tool to write/update the same set of keys repeatedly as one process and have the redis benchmark run as a separate process to execute reads at the same time.

The primary purpose of this additional tool is to enable the writing of a limited number of sequential keys into Redis so that when reading, you can be more certain of the ratio of read misses to hits that happen.

If you write 10,000 sequential keys to redis (the default) and then read 100,000 using benchmark you will get a hit ratio of 1/10.




