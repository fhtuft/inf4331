#!/bin/bash  

# Gets a page with wget (uses ruter.no with "se avgange i sandtid", station name entered in fild, Nydalen or Blinder), uses grep to get line with info
#For east and west, uses parameter expansion to get the line after or before "Retning Sognsvann" 
#Then uses grep with display text mode(not line) to grap departureTime:[digit][digit]:[digit][digit], uses new grep to extract only the time

#Check that one or less arg is given 
if(( $# > 1)); then
    echo "To many args!"
    exit
fi
#if one arg is given
if(( $# > 0))
then
    case $1 in

# --Blindern East-- #
    --E)
        page=$(wget -q -O -  https://ruter.no/reiseplanlegger/Stoppested/%283010360%29Blindern%20%5BT-bane%5D%20%28Oslo%29/Avganger/#st:1,sp:0,bp:0 | grep "BoardingAllowed")

        page=${page##*"Retning Sognsvann"}
        echo "East (Sognsvann/Storo) Blindern"
        echo "$page" | grep -oh \"departureTime\":\"[0-9][0-9]:[0-9][0-9] |grep -oh [0-9][0-9]:[0-9][0-9] 
        exit
        ;;

# --Blinder West-- #    
    --W)
        page=$(wget -q -O -  https://ruter.no/reiseplanlegger/Stoppested/%283010360%29Blindern%20%5BT-bane%5D%20%28Oslo%29/Avganger/#st:1,sp:0,bp:0 | grep "BoardingAllowed")

        page=${page%%"Retning Sognsvann"*}
        echo "West (Majorstua) Blindern"
        echo "$page" | grep -oh \"departureTime\":\"[0-9][0-9]:[0-9][0-9] |grep -oh [0-9][0-9]:[0-9][0-9] 
        exit
        ;;
    
# --Nydalen all directions-- #
    Nydalen)

        page=$(wget -q -O - https://ruter.no/reiseplanlegger/Stoppested/%283012130%29Nydalen%20%5BT-bane%5D%20%28Oslo%29/Avganger/#st:1,sp:0,bp:0 | grep "BoardingAllowed" | grep -oh \"departureTime\":\"[0-9][0-9]:[0-9][0-9] |grep -oh [0-9][0-9]:[0-9][0-9] )

        echo "Departue times  from Nydalen"
        echo "$page"
        exit
        ;;
    #Unknow arg #
    *)
        echo "Wrong options!"
        exit
    esac
fi

# --Blinder all directions-- #

page=$(wget -q -O -  https://ruter.no/reiseplanlegger/Stoppested/%283010360%29Blindern%20%5BT-bane%5D%20%28Oslo%29/Avganger/#st:1,sp:0,bp:0 | grep "BoardingAllowed" | grep -oh \"departureTime\":\"[0-9][0-9]:[0-9][0-9] |grep -oh [0-9][0-9]:[0-9][0-9] )
echo "Departure times for  from Blinder"
echo "$page"


