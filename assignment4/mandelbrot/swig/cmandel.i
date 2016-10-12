%module cmandel

%{
    #define SWIG_FILE_WITH_INIT
    #include "cmandel.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (int DIM1,int* IN_ARRAY1){(int dim,int* array)};
%include "cmandel.h"
