FOLDER_PATH = ~/My_Projects/pucrs

bash:
	docker run -v $(FOLDER_PATH):/pucrs -t -i jflexbyacc /bin/bash

image:
	docker build -t jflexbyacc .
