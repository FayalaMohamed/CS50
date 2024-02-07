#include <cs50.h>
#include <stdio.h>
#include <math.h>

long power (int n)
{
    long y=1;
    for(int i=0;i<n;i++){
        y=y*10;
    }
    return y;
}

int digit(long x, int n)
{
    int digit=0;
    if(n==1){
        digit=x%10;
    }else if(n>1)
    {
        /*long y=x%power(n);
        long z=x%power(n-1);

        digit=(y-z)/power(n);*/
        x=x/power(n-1);
        digit=x%10;
    }
    return digit;
}

int main(void)
{
    long ccnumber =get_long("Credit card number ");
    printf("%i \n",digit(ccnumber,4));
}