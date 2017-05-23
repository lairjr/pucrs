bash:
	docker run -v ~/My_Projects/pucrs:/pucrs -t -i java /bin/bash

image:
	docker build -t java .
