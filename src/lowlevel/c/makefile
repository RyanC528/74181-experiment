chip:
	gcc -I. -g -O -c chip.c chip.h

control:
	gcc -I. -g -O -c control.c control.h

main:
	gcc -o main chip.o control.o

cleanup:
	rm edit $(objects)
