source .env $NATS_AUTH_TOKEN
nats-server --tls --tlscert=./cert.pem --tlskey=./key.pem --auth $NATS_AUTH_TOKEN 

