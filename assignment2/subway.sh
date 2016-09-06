#!/bin/bash  

if(( $# > 0))
then
case $1 in
--E)
    echo "East"
    exit
    ;;
--W)
    echo "West"
    exit
    ;;
    
Nydalen)
    echo "Nydalen"
    exit
    ;;

esac

fi

page=$(wget -O -  https://ruter.no/reiseplanlegger/Stoppested/%283010360%29Blindern%20%5BT-bane%5D%20%28Oslo%29/Avganger/#st:1,sp:0,bp:0 | grep "BoardingAllowed" | grep -oh \"departureTime\":\"[0-9][0-9]:[0-9][0-9] |grep -oh [0-9][0-9]:[0-9][0-9] )

#page=${page%%*departureTime}
echo "Departue time for next lines from Blinder"
echo "$page"


