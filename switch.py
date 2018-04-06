#!/bin/bash
#auther:fanxuanhui

USAGE(){
	echo "Usage: .$0 [ to2 | to3 ]"
	echo "to2 : switch to python2.7"
	echo "to3 : switch to python3.5"
}

if [[ $1 == "to3" ]]
then
	if [ -L /usr/bin/python ]
	then
		echo "亲 ! 已经是python3 了"
	else 
		mv /usr/bin/python{,2.7-xx}
		ln -sv /usr/local/python3/bin/python3.5 /usr/bin/python
	fi

elif [[ $1 == to2 ]]
then
	if [ -L /usr/bin/python ]
	then
		unlink /usr/bin/python
		mv /usr/bin/python2.7-xx /usr/bin/python
	else
		echo "亲 ！已经是python2 了"
	fi
else
	if [ -L /usr/bin/python ]
	then
		echo -e "\033[32m 当前python版本是3.5 \033[0m "
		USAGE
	else
		echo -e "\033[32m 当前python版本是2.7 \033[0m "
		USAGE
	fi

fi

