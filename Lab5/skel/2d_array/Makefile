build:
	gcc eliminate_constants.c -o eliminate_constants -g -Wall -O0
	gcc blocked_matrix_multiplication.c -o blocked_matrix_multiplication -g -Wall -O0
	gcc i-k-j.c -o i-k-j -g -Wall -O0
	gcc j-i-k.c -o j-i-k -g -Wall -O0
	gcc j-k-i.c -o j-k-i -g -Wall -O0
	gcc k-i-j.c -o k-i-j -g -Wall -O0
	gcc k-j-i.c -o k-j-i -g -Wall -O0

run1:
	run ./eliminate_constants

run2:
	run ./blocked_matrix_multiplication

clean:
	rm eliminate_constants blocked_matrix_multiplication i-k-j j-i-k j-k-i k-i-j k-j-i