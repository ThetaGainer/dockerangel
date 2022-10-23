## AngelAlgo Docker Guide

Step1: Build the docker image and run the container:
```
wget https://raw.githubusercontent.com/ThetaGainer/dockerangel/main/Dockerfile && docker build -t angel . && docker container run --rm -i -t --net=host --name angelalgo angel
```

Step 2: Run the code
```
python3 Algo.py
```
