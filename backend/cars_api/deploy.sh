docker build -t cars-api .
docker tag cars-api:latest 040508513186.dkr.ecr.us-west-2.amazonaws.com/cars-api:latest
docker push 040508513186.dkr.ecr.us-west-2.amazonaws.com/cars-api:latest
