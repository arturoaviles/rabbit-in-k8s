env:
	bash -c "set -a && source .env && set +a"

build:
	docker build -t aavilesndscognitivelabs/productor:latest ./productor
	docker build -t aavilesndscognitivelabs/consumidor:latest ./consumidor

push:
	docker push aavilesndscognitivelabs/productor:latest
	docker push aavilesndscognitivelabs/consumidor:latest

