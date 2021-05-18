#!/bin/bash
#Mary deMarigny
#Base Decoder
#03/18/2021

	##### If ASCII Cypher #####

#checks if the code is encrypted with ASCII
ASCII_check(){
	printf "\nchecking for ASCII encryption"
	#checks for ASCII base 32 and 64 encryption
	for i in 32 64
		do
		printf "\nBase-$i: \n"
		base="base$i"
		echo $codeToCrack | $base -d
		i=$[1+$i]
	done
	#check if that was right
	printf "\nWas the code cracked? If so, which base? (N/32/64) "
	read response

	#depending on the answer, move on approptiately
	case $response in
		N)
			#check for Ceasar Cypher
			Caesar_check codeToCrack file;;
		32)
			ASCII_decrypt 32 file;;
		64)
			ASCII_decrypt 64 file;;
		*)
			printf "only N, 32, and 64 were acceptable responses\n"
			ASCII_check codeToCrack
	esac
}

#decrypts all the code and saves it to a document
ASCII_decrypt(){
	base="base$1"
	printf "\nWhat is the file type?\n"
	read fileType
	printf "What do you want to name the file?\n(do not include the file extention)\n"
	read fileName
	saveFile="$fileName.$fileType"
	echo $saveFile
	echo | tr -d '\n' < $file | $base -d >> $saveFile
}


	##### If Caesar Cypher ##### 
Caesar_check(){
	i=1
	prev=a
	for char in b c d e f g h i j k l m n o p q r s t u v w x y z
		do
		echo "rot-$i"
		echo $codeToCrack | tr a-z $char-za-$prev
		printf "\n"
		#save previous character to be used next round
		prev=$char
		i=$[$i+1]
	done

	printf "Was it Caesar Cypher? If so, what rot? (N/1/2/3/etc.)\n"
	read response
	#to check for numbers
	num='^[0-9]'
	#depending on the answer, move on approptiately
	case $response in
		N)
			#check for the next Cypher
			;;
		*)
			Ceaser_decrypt response file;;
	esac

}

Ceaser_decrypt(){
	
	printf "\nWhat is the file type?\n"
	read fileType
	printf "What do you want to name the file?\n(do not include the file extention)\n"
	read fileName
	saveFile="$fileName.$fileType"
	echo $saveFile
	echo | tr -d '\n' < $file | tr a-z $char-za-$prev >> $saveFile
}


### Entry Point ###

#check for input
if [ $# == 0 ]; then
	#if no arguments are given, a usage statement is printed
	echo "Usage: bash $0 file.extension"
else
	#save file and the first 2 lines of the file
	file=$1
	codeToCrack=$(head -n 2 $file)
	#check ASCII first
	ASCII_check codeToCrack file
fi