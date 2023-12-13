import redis,sys,os 

'''
You may start this script with an argument that 
indicates how many batches of 10K keys to write to Redis. 
To write 50 batches of 10K keys (500,000 total keys) you would do this:

python3 sequentialBenchmarkkeys.py 50

(Each key take up about 100bytes of memory)
'''
redishost = 'FIXME.southcentralus.redisenterprise.cache.azure.net'
redispassword = 'VakhcJeA8U4PLjA1uThXexC8ql98Ov2BtVvVj76KBfQot='
redisport = 10000
redisuser = 'default'
CERT_DIR = '/tmp/certs'
SERVER_CERT = os.path.join(CERT_DIR,"redis-client-cert.pem")
SERVER_KEY = os.path.join(CERT_DIR,"redis-client-key.pem")
CACERTS = os.path.join(CERT_DIR, "ca.pem")

# if using TLS:
#redisProxy = redis.StrictRedis(redishost,redisport, username=redisuser,password=redispassword, charset="utf-8", decode_responses=True, ssl=True,ssl_certfile=SERVER_CERT,ssl_keyfile=SERVER_KEY,ssl_ca_certs=CACERTS)
# if not using TLS:
redisProxy = redis.StrictRedis(redishost,redisport,password=redispassword, charset="utf-8", decode_responses=True)
 
# Function to reverse a string
def reverse(string):
    string = "".join(reversed(string))
    return string

def writeSequentialBenchmarkStringKeys(loop_count,startvalue, stopvalue):
  counter = startvalue
  keynamebase='000000000000'
  pipe = redisProxy.pipeline()
  while (counter<=stopvalue):
    kname = reverse((reverse(keynamebase+str(counter)))[0:12])
    counter = counter+1
    pipe.set('key:'+kname+'{'+str(loop_count)+'}','https://imadummyuri'+str(counter)+'pad100 bytes')
  pipe.execute()
    


if __name__ == "__main__":
    loop_count=1
    if len(sys.argv)>1:
      #we are expecting an integer to drive the loop of batch writes
      loop_count=int(sys.argv[1])
    print(f"starting to write {loop_count} X 10K small strings")
    # this line starts the execution of repeated writes in batches of 10k:
    for i in range(loop_count):
      writeSequentialBenchmarkStringKeys(loop_count,1,10000)
