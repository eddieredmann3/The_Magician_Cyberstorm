
cypher (){
	cypher=""
	for i in message
		do
		if [ message[i] = key[i] ]; then
			cypher="${cypher}0"
		else
			cypher="${cypher}1"
		fi
	done
	printf "cypher = $cypher"
}


### Entry Point ###

#check for input
if [ $# == 0 ]; then
	#if no arguments are given, a usage statement is printed
	echo "Usage: key"
else
	#save file and the first 2 lines of the file
	key=$1
	
	printf "\nWhat is the mesage?\n"
	read message

	#check ASCII first
	cypher key message
fi
