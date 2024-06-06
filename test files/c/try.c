#include <stdio.h>
#include <stdbool.h>
  
void main () {
	char a[]="hello world!!";
	int i,n;
	char *p;
	char x,q;
	bool y;
	n=0;
	for (p=a;*p++;) {
		n++;
	}
	n--;
	y=true;
	while (y==true) {
		for (i=0;i<n;i++) {
			y=false;
			if (a[i+1]<a[i]) {
				x=a[i];
				q=a[i+1];
				a[i]=q;
				a[i+1]=x;
				y=true;
			}
		}
	} 
	for (i=0;i<=n;i++) {
		printf("%c",a[i]);
	} 
	printf(" \n");
}
