## WhaleHoney
A Flask application to emulate the Docker API for honeypot purposes.
Released as apart of ATT&CKCon 3.0 presentation, ATT&CKing Containers in The Cloud.

* Inspired by Cisco SIRT's [dhp](https://github.com/ciscocsirt/dhp).
* Inspired by [Whaler](https://github.com/oncyberblog/whaler)

### How does it work?
Whalehoney mocks some API endpoints detailed within the official [Docker
Engine API guide](https://docs.docker.com/engine/api/v1.41/). Incoming requests are logged to ```whalehoney-YYYY-MM-dd.log```.
No operation is performed on the incoming request other than logging it to a plaintext file.

### How to run

1. Create a virtual environment.

```
python3 -m venv venv
```

2. Use virtual env.

```
source ./venv/bin/activate
```

3. Install Python dependencies.

```
pip3 install -r requirements.txt
```

4. (without gunicorn) Start whalehoney.

```
python3 wsgi.py
```

4. (with gunicorn) start whalehoney.

```
python3 wsgi.py --bind=0.0.0.0:2375
```


### Build & Run from Dockerfile
1. Build the container
```
docker build . -t whalehoney:latest
```

2. Run the container exposing the Docker port (2375) to the honeypot
```
docker run -p 2375:2375 --name whalehoney whalehoney:latest -d
```

### Interacting with API Endpoints
Test endpoints to ensure the container is running:
```
$> curl localhost:2375/version;
$> curl localhost:2375/_ping;
```

Docker logs available within the conatiner at: ```./logs/$DATE/whalehoney-$DATE.log```

*Reference the dockerapi/dockeroutes.py for more*
