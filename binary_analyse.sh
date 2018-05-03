#!/bin/bash

# file
bin=${1}
f=$(file $bin)
bit=$(echo $f | cut -d " " -f3)
elf=$(echo $f | cut -d " " -f2)
intel=$(echo $f | cut -d " " -f6)
intel="$intel $(echo $f | cut -d " " -f7)"
strip=$(echo $f | cut -d " " -f19)
strip="$strip $(echo $f | cut -d " " -f20)"
echo $bit $elf"," $intel $strip

# strings
func=""
string=$(strings $bin)
for i in $string
do
	#echo $i
	if [ $i = "strcpy" ]; then
		func="strcpy, $func"
	fi
	if [ $i = "strncpy" ]; then
		func="strncpy, $func"
	fi
	if [ $i = "system" ]; then
		func="system, $func"
	fi
	if [ $i = "execve" ]; then
		func="execve, $func"
	fi
	if [ $i = "execlp" ]; then
		func="execlp, $func"
	fi
	if [ $i = "execve" ]; then
		func="execve, $func"
	fi
	if [ $i = "execv" ]; then
		func="execv, $func"
	fi
	if [ $i = "execvp" ]; then
		func="execvp, $func"
	fi
	if [ $i = "popen" ]; then
		func="popen, $func"
	fi
	if [ $i = "gets" ]; then
		func="gets, $func"
	fi
	if [ $i = "fgets" ]; then
		func="fgets, $func"
	fi
	if [ $i = "strcmp" ]; then
		func="strcmp, $func"
	fi
done
echo "Vuln funcs: "$func

#readelf
if [[ $bit =~ "32" ]]; then
	readelf=$(readelf -l $bin | grep "GNU_STACK" | cut -d " " -f14)
	if [[ $readelf =~ "E" ]]; then
		echo "Stack is executable"
	fi
else
	if [[ $bit =~ "64" ]]; then
		readelf=$(readelf -l $bin | grep -A1 "GNU_STACK")
		readelf=$(echo $readelf | cut -d " " -f7)
		if [[ $readelf =~ "E" ]]; then
			echo "Stack is executable"
		fi
	fi
fi