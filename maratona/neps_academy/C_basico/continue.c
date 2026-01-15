#include<stdio.h>
int main (){
	int i;
	for(int i = 0; i < 6; i++){
		if(i == 2){
			continue;
		}
		printf("%d\n", i);
	}
}