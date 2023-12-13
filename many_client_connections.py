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
