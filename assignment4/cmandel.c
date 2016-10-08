#include <stdio.h>
#include <stdlib.h>
#include <math.h>


double **solver(const double xmin,const double xmax,const double ymin, const double ymax, const int Nx,const int Ny,const int max_escape_time) 
{

    /* Make the result matrix */
    const size_t sizeof_array = sizeof(int)*Ny*Nx;
    int *array = (int*)malloc(sizeof_array);
    memset(array,0,sizeof_array);
    int **matrix = (int**)malloc(sizeof(int*)*Ny);
    for(int i =  0,int*tmp = array; i<Ny; i++) {
        matrix[i]=tmp;
        tmp+=Nx
    }

    for(int j = 0; j<Ny; j++) {
        for(int i = 0; i<Nx; i++) {
            const index = j*Nx+i;
            int time = 0;
            const double x = i*((xmax-xmin)/Nx);
            const double y = j*((xmax-xmin)/Ny);
            double a = 0.0,b =0.0;
            while(time < max_escape_time) {
                a = a*a-b*b + x;
                b = 2*a*b + y;                                
                if(a*a + b*b > 4.0) break;

                time++;
            }    
                array[index] = time;
        }    
    }

    return matrix
}



#ifdef CMAIN

int main(int argc, char *argv[]) {
    
     

    return 0;
}
#endif


