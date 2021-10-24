#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void exit(int status);

char flag[39] = "vuctf{wont_you_take_me_to_func_ytown?}\x00";

char *vuln(void)
{
    char buf[16];
    scanf("%s", buf);
}

int main()
{
    setbuf(stdout, 0);
    printf("Welcome to funky town!\nEnter your name: ");
    vuln();
    printf("Sorry, is that even your real name?\n");
    return 0;
}

void ytown()
{
    printf("\nCongrats, the flag is %s\n", flag);
    exit(0);
}
