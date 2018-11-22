#include <stdio.h>
#include <stdlib.h>
/****************************************************************/
void fun(char *s) {
//	char *s=string;
	int sum=1;
	int len=sizeof(s)/sizeof(s)[0];
	for(int i=0; i<len; i++) {
//		if (s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'|| \
//		        s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U') {
//			sum+=(len-i)*(i+1);
		printf("%s",s[i]);
//		}
	}
//	return sum;
}
int main(void) {
	int t;      //t为输入行数
	scanf("%d",&t);
	printf("\n");
	for(int i=0; i<t; i++) {
		char s[10];
		scanf("%s",&s);
		int sum=0;
		/*sum=*/fun(s);
//		printf("%d",sum);
	}
	return 0;
}

