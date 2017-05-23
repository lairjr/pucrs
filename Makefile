FOLDER_PATH = ~/My_Projects/pucrs

bash:
	docker run -v $(FOLDER_PATH):/pucrs -t -i java /bin/bash

image:
	docker build -t java .
