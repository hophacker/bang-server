vpath %.cpp .
CC=g++
CFLAGS=-g

_TAR = hello
_OBJ = $(patsubst %,%.o,$(_TAR)) 

TAR = $(patsubst %,obj/%,$(_TAR))
OBJ = $(patsubst %,obj/%,$(_OBJ))

.PHONY: all clean print test debug

all: $(TAR)

print: 
	echo $(OBJ) $(TAR)

debug:
	./obj/hello
test:
	./obj/hello 2>error

$(TAR):$(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
	
$(OBJ): | obj

obj:
	@mkdir -p $@

obj/%.o : %.cpp %.h
	@echo $<
	$(CC) -c -o $@ $< $(CFLAGS)


.PHONY : clean
clean:
	rm -rf *.o obj/ 
