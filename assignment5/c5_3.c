//This is a one line comment

/* 
    This is a multiline comment
*/

//include 
#include <stuff.h>
//more include
#include "moreStuff.h"

char str[] = "This is a string";

int main(int argc, char *argv[]) {
    
    int i = 0;
    long int l;
    long  long  int l;
    unsigned int u;
    short s;
    char c;
    double d;
    float f; 
    for(i = 0; i<10; i++) {

    }

    while(i<100) {
        i++;
    }

    do {
        i++;
    }while(i < 1000);
    
    if(i == 1000) {
        fprintf(stderr,"hi!\n");
    }else if(i == 10001) {
        printf("Hi more!\n");
    }else {
        printf("Hi even more!\n")
    }


#define THISISADEFINE 1
    goto LABEL;

LABEL:
    return ;

}

