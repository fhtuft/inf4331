#!/bin/bash

# Check that some arguments are given #
if(($# < 1)) 
then
    echo "No args given "
    exit
fi



# Check witch operation should be done #
case $1 in
# Sum #
S)
    #echo "S!"
    shift
    if (( $# <= 1 ))
    then
        echo "Sum must have min 2 numbers"
        exit
    fi
    declare -i sum=$1
    shift

    while [[ $# > 0 ]] ; do
        sum=$(($sum + $1 ))
        shift    
    done   
    echo $sum 
    ;;
# Product #
P)
    #echo "P!"
    shift
      if (( $# <= 1 ))
    then
        echo "Product must have min 2 numbers"
        exit
    fi
    declare -i product=$1
    shift
    while [[ $# > 0 ]] ; do
        product=$(($product * $1 ))
        shift    
    done   
    echo $product 
    ;;
# Max #
M)
    #echo "M!"
    shift
    if (( $# < 1 ))
    then
        echo "Max must have min 1 numbers"
        exit
    fi
    declare -i max=$1
    shift
    while [[ $# > 0 ]] ; do
        if (($1 > $max))
        then
            max=$1
        fi
        shift    
    done   
    echo $max
    ;;
# Min #
m)
    #echo "m!"
    shift
    if (( $# < 1 ))
    then
        echo "Min must have min 1 numbers"
        exit
    fi
    declare -i min=$1
    shift
    while [[ $# > 0 ]] ; do
        if (($1 < $min))
        then
            min=$1
        fi
        shift    
    done   
    echo $min
    ;;
*)
    echo "$1 is not a valid op"
    exit
    ;;
esac
