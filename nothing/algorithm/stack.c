#include<stdio.h>
#include<stdlib.h>


int stack[10000];
int top = -1;

void push(int data){
	stack[++top] = data;
}

int pop(){
	if(top == -1)
		return printf("%d\n",-1);
	return printf("%d\n",stack[top--]);
}

int size(){
	return printf("%d\n",top+1);
}

int empty(){
	if(top==-1){
		return printf("%d\n",-1);
	return printf("%d\n",0);
}
}
int func_top(){
	return printf("%d",stack[top]);
}

int main(){
	int s = 0;
	scanf("%d",&s);
	for(int k =0; k<s; k++){
		char a[100];
		scanf("%s",&a);
		if(strcmp(a,"push")==0){
			int b;
			scanf("%d",&b);
			push(b);
		}
		else if(strcmp(a,"pop")==0){
			pop();
		}
		else if(strcmp(a,"size")==0){
			size();
		}
		else if(strcmp(a,"empty")==0){
			empty();
		}
		else if(strcmp(a,"top")==0){
			func_top();
		}
		else if(strcmp(a,"quit")==0){
			break;
		}
	}
}
