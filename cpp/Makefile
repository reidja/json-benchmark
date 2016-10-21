CC=g++
CFLAGS=-I.

all: runner

runner: runner.c
	$(CC) -O2 -o runner runner.c -I rapidjson/include

clean:
	$(RM) runner