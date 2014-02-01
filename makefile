vpath %.cpp .
CC=g++
CFLAGS=-g
obj_dir=cgi-bin

_TAR = hello
_OBJ = $(patsubst %,%.o,$(_TAR)) 

TAR = $(patsubst %,$(obj_dir)/%,$(_TAR))
OBJ = $(patsubst %,$(obj_dir)/%,$(_OBJ))

.PHONY: all clean print test debug

all: $(TAR)

print: 
	echo $(OBJ) $(TAR)

debug:
	./$(obj_dir)/hello
test:
	./$(obj_dir)/hello 2>error

$(TAR):$(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
	
$(OBJ): | $(obj_dir)

$(obj_dir):
	@mkdir -p $@

$(obj_dir)/%.o : %.cpp %.h
	@echo $<
	$(CC) -c -o $@ $< $(CFLAGS)


.PHONY : clean
clean:
	rm -rf *.o $(obj_dir)/ 
