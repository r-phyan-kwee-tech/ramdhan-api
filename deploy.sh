docker rm ramdan_api

docker build ./ -t ramdan_api

docker run --name ramdan_api -p 80:5000 ramdan_api
