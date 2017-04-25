image:
	docker build -t lab-redes .
compile:
	docker run -t -i -w /pucrs/t1 -v ~/My_Projects/pucrs:/pucrs lab-redes gcc sniffer.c -o sniffer
sniffer: compile
	docker run -t -i -w /pucrs/t1 -v ~/My_Projects/pucrs:/pucrs lab-redes ./sniffer
