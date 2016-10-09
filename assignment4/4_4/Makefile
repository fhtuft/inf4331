CC = gcc
CFLAG = -Wall -O0 -std=gnu99 

LINKER = gcc -o
LFLAGS = 

bin = cmandel_test

RM = rm -f

all: cmandel.o  

%.o: %.c
	$(CC) $< $(CFLAG) -c -o $@

cmandel_test: cmandel.c
	$(CC) $< $(CFLAG) -DCMAIN   -o $@

run:
	./cmandel_test

clean:
	$(RM) $(bin)