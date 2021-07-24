#include<stdio.h>
#include<string.h>
void main()
{
	int result;
	char str1[20],str2[20];
	scanf("%s",str1);
	scanf("%s",str2);
	result=stricmp(str1,str2);
	if(result>0)
	printf("1");
	else if(result<0)
	printf("-1");
	else
	printf("0");
}
