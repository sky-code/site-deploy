
build: COMMIT=$(shell git rev-parse HEAD)
build: BUILD_TIME=$(date)
build:
	docker build site-deploy -t site-deploy --build-arg COMMIT=$(COMMIT) --build-arg BUILD_TIME="$(BUILD_TIME)"
