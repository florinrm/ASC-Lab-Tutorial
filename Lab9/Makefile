build:
	nvcc main.cu -o main -lm
	nvcc main-unified.cu -o main-unified -lm
	nvcc atomic.cu -o atomic
	nvcc dynamic.cu -o dynamic
	nvcc async.cu -o async

clean:
	rm main-unified main atomic dynamic async