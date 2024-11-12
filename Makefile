docker :
	docker build . -t juleslatapy1/example-app-2:$(VERSION)
	docker push juleslatapy1/example-app-2:$(VERSION)