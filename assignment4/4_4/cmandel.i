%module cmandel

%{
    #define SWIG_FILE_WITH_INIT
    #include "cmandel.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (int* INPLACE_ARRAY1, int DIM1){(int* array,int dim)}
%include "cmandel.h"
