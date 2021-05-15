APP_NAME = dict

CC = g++
CFLAGS = -Wall -std=c++14

TEST_CFLAGS = -fsanitize=leak
DEBUG_CFLAGS = $(TEST_CFLAGS) -Werror -D DEBUG -O0

TARGET = src/main.cpp 

default:
	$(CC) $(CFLAGS) -o $(APP_NAME).out $(TARGET)

test: 
	$(CC) $(CFLAGS)  $(DEBUG_CFLAGS)-o $(APP_NAME).out $(TARGET)

clean:
	rm $(APP_NAME).out
