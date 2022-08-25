import redis,os

redishost = 'redis-10000.homelab.local'
redispassword = ''
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

def writeSequentialBenchmarkStringKeys(startvalue, stopvalue):
  counter = startvalue
  keynamebase='000000000000'
  while (counter<=stopvalue):
    kname = reverse((reverse(keynamebase+str(counter)))[0:12])
    counter = counter+1
    redisProxy.set('key:'+kname,'https://imadummyuri'+str(counter))

for i in range(100):
    writeSequentialBenchmarkStringKeys(0,10000)
