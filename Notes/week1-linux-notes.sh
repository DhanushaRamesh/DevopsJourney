#!/bin/bash
echo "Dispaly the current path : pwd"
pwd
echo "Dispaly all the files in the path : ls"
ls
echo "Dispaly all the files in the path except hidden directories : ls -la"
ls -la
echo "Command to create new directories : mkdir"
mkdir testing
echo "Command used for moving to folders/directories : cd"
cd testing
echo "Command used for creating new file : touch"
touch test.txt
echo "Command used for copying files : cp"
cp test.txt newname.txt
echo "Command to move the files : mv"
mv newname.txt ../
echo "Command to remove files : rm"
rm ../newname.txt
echo "Command to remove directories : rm -r"
rm -rf ../testing
echo "Command to clear the terminal : clear" #try using in the terminal 