#!/bin/bash

echo "!!!!!!!!!!!!!!!! Assignemt 5 5 !!!!!!!!!!!!!!!!!!!"
echo "!!!!!!!!!!!!!!!! addition !!!!!!!!!!!!!"
python3 colour_diff.py diffTests/1add1.txt diffTests/1add2.txt diff.theme
echo "!!!!!!!!!!!! Two additions !!!!!!!!!!!!!!!!!!1"
python3 colour_diff.py diffTests/2add1.txt diffTests/2add2.txt diff.theme
echo "!!!!!!!!!!!!!!!!!! Delition !!!!!!!!!!!!!!!!!!!!11"
python3 colour_diff.py diffTests/1del1.txt diffTests/1del2.txt diff.theme

echo "!!!!!!!!!!!!!! Permutation !!!!!!!!!!!!!!!!!11"
python3 colour_diff.py diffTests/1perm1.txt diffTests/1perm2.txt diff.theme

echo "!!!!!!!!!!!!!!!! complitly different !!!!!!!!!!!!!!!!!!!!"
python3 colour_diff.py diffTests/comp1.txt diffTests/comp2.txt diff.theme

echo "!!!!!!!!!!!! Samme !!!!!!!!!!!!!!!!"
python3 colour_diff.py diffTests/same.py diffTests/same.py diff.theme







