build:
	nvcc main.cu -o main_cuda -lm
	gcc main.c -o main -lm -std=gnu99
	nvcc hello.cu -o hello
	
clean:
	rm main_cuda main hello