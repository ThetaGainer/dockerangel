## AngelAlgo Docker Guide

Step1: Build the docker image:
```
wget https://raw.githubusercontent.com/ThetaGainer/dockerangel/main/Dockerfile && docker build -t angel .
```

Step2: Run the docker container:
```
docker container run --rm -i -t --name angelalgo angel
```

Step 3: Run the code
```
python3 Algo.py
```
