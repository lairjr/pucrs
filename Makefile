bash:
	docker run -v ~/My_Projects/compiladores:/compiladores -t -i java /bin/bash

image:
	docker build -t java .
