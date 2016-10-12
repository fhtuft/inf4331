#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void solver(int dim,int *array,double xmin,double xmax,double ymin,double ymax,int Nx,int Ny,int max_escape_time) 
{

	
	int i,j;
   	 for(j = 0; j<Ny; j++) {
        	for(i = 0; i<Nx; i++) {
            	const int index = j*Nx+i;
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

}



#ifdef CMAIN

int main(int argc, char *argv[]) {
    
   
	const double ymin = -2.0;
	const double ymax = 2.0;
 	const double xmin = -2.0;
 	const double xmax = 2.0;
	const int Nx = 100;
	const int Ny = 100;
	const int max_escape_time = 100;
    	/* Make the result matrix */
    	const size_t sizeof_array = sizeof(int)*Ny*Nx;
    	int *array = (int*)malloc(sizeof_array);
    	memset(array,0,sizeof_array);
    	int **matrix = (int**)malloc(sizeof(int*)*Ny);
	int *tmp = array;
    	for(int i = 0; i < Ny; i++) {
        	matrix[i]=tmp;
        	tmp+=Nx;
    	}
  	solver(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,matrix);

	/*Print out mandelbrot*/
	for(int j = 0; j< Ny; j++) {
		printf("\n");
		for(int i = 0; i<Nx; i++) 
			printf("%d ",matrix[j][i]);
	}	

 

    	return 0;
}
#endif


