#!/bin/bash  

if(( $# > 0))
then
case $1 in
--E)
    page=$(wget -q -O -  https://ruter.no/reiseplanlegger/Stoppested/%283010360%29Blindern%20%5BT-bane%5D%20%28Oslo%29/Avganger/#st:1,sp:0,bp:0 | grep "BoardingAllowed")


page=${page##*"Retning Sognsvann"}
echo "East (Sognsvann/Storo) Blindern"
echo "$page" | grep -oh \"departureTime\":\"[0-9][0-9]:[0-9][0-9] |grep -oh [0-9][0-9]:[0-9][0-9] 
    exit
    ;;
--W)
    
    page=$(wget -q -O -  https://ruter.no/reiseplanlegger/Stoppested/%283010360%29Blindern%20%5BT-bane%5D%20%28Oslo%29/Avganger/#st:1,sp:0,bp:0 | grep "BoardingAllowed")


page=${page%%"Retning Sognsvann"*}
echo "West (Majorstua) Blindern"
echo "$page" | grep -oh \"departureTime\":\"[0-9][0-9]:[0-9][0-9] |grep -oh [0-9][0-9]:[0-9][0-9] 
   
    exit
    ;;
    
Nydalen)
page=$(wget -q -O - https://ruter.no/reiseplanlegger/Stoppested/%283012130%29Nydalen%20%5BT-bane%5D%20%28Oslo%29/Avganger/#st:1,sp:0,bp:0 | grep "BoardingAllowed" | grep -oh \"departureTime\":\"[0-9][0-9]:[0-9][0-9] |grep -oh [0-9][0-9]:[0-9][0-9] )

#page=${page%%*departureTime}
echo "Departue times  from Nydalen"
echo "$page"

    exit
    ;;

esac

fi

page=$(wget -q -O -  https://ruter.no/reiseplanlegger/Stoppested/%283010360%29Blindern%20%5BT-bane%5D%20%28Oslo%29/Avganger/#st:1,sp:0,bp:0 | grep "BoardingAllowed" | grep -oh \"departureTime\":\"[0-9][0-9]:[0-9][0-9] |grep -oh [0-9][0-9]:[0-9][0-9] )

#page=${page%%*departureTime}
echo "Departure times for  from Blinder"
echo "$page"


