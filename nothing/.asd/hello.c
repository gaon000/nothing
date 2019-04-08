#include<stdio.h>
int main(){
	FILE *file;
	file = fopen("a.txt",'w');
	fputs("hello world",pfile);
	fclose(pfile);
	return 0;
}
