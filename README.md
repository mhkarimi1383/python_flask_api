# python_flask_api
### Flask API with python Dockerized

## How get it up & running
> **NOTE** Before starting these proccess you should install docker
1. clone the repo and change directory to that
```bash
git clone https://github.com/mhkarimi1383/python_flask_api 
cd python_flask_api
```
2. build Docker image
```bash
docker build -t my_own_flask .
```
3. run a container based on built image
```bash
docker run -d -p 5000:5000 my_own_flask
```
