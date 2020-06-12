#!/bin/bash

PROJECTOR_HOSTNAME='projektor'

display_help()
{
	echo "Usage: $0 [option...] <command> <setting> [<parameter>]" >&2
	echo
	echo "  -h, --help	Show this message"
	echo "  -f, --force"
	echo
	echo "Commands:"
	echo "  get <setting>"
	echo "  set <setting> <on|off>"
	echo "  switch <setting>"
	echo
	echo "Settings:"
	echo "  power"
	echo "  mute"
	echo "  freeze"
	echo
	echo "Examples:"
	echo "  get mute"
	echo "  set freeze on"
	echo "  switch power"
	exit 1
}

send_request()
{
	D=""
	for a in $@
	do
		D="$D%$a"
	done
	URL="http://$PROJECTOR_HOSTNAME/cgi-bin/pjctrl.cgi.elf?D=$D"
	echo $(curl -s $URL | sed 's/\[//; s/\]//' | xargs -d ',')
}

get_power()
{
	STATUS=(`send_request 06 00 85 00 00 01 01 87`)
	echo ${STATUS[7]}
}

set_power()
{
	if [[ $1 -eq 1 ]];
	then
		STATUS=`send_request 05 02 00 00 00 00`
	else
		STATUS=`send_request 05 02 01 00 00 00`
	fi
}

switch_power()
{
	STATUS=`get_power`
	if [[ $STATUS -eq 1 ]];
	then
		STATUS=`set_power 0`
	else
		STATUS=`set_power 1`
	fi
}

get_mute()
{
	STATUS=(`send_request 06 00 85 00 00 01 03 89`)
	echo ${STATUS[5]}
}

set_mute()
{
	if [[ $1 -eq 1 ]];
	then
		STATUS=`send_request 05 02 10 00 00 00 13`
	else
		STATUS=`send_request 05 02 11 00 00 00 13`
	fi
}

switch_mute()
{
	STATUS=`get_mute`
	if [[ $STATUS -eq 1 ]];
	then
		STATUS=`set_mute 0`
	else
		STATUS=`set_mute 1`
	fi
}

get_freeze()
{
	STATUS=(`send_request 06 00 BF 00 00 01 02 C2`)
	echo ${STATUS[14]}
}

set_freeze()
{
	if [[ $1 -eq 1 ]];
	then
		STATUS=`send_request 06 01 98 00 00 01 01 00`
	else
		STATUS=`send_request 06 01 98 00 00 01 02 00`
	fi
}

switch_freeze()
{
	STATUS=`get_freeze`
	if [[ $STATUS -eq 1 ]];
	then
		STATUS=`set_freeze 0`
	else
		STATUS=`set_freeze 1`
	fi
}


# options
while :
do
	case "$1" in
		-h | --help)
			display_help
			exit 0
			;;
		-f | --force)
			echo "Nothing to force, man"
			shift
			;;
		--)
			shift
			break
			;;
		-*)
			display_help
			exit 1
			;;
		*)
			break
			;;
	esac
done

# commands
case "$1" in
	get | set | switch)
		FNAME="$1_$2"
		if [[ `type -t $FNAME` == '' ]]
		then
			echo "Invalid parameter for $1"
			display_help
			exit 1
		fi
		OPT=`sed 's/on/1/; s/off/0/' <<< $3`
		$FNAME $OPT
		;;
	*)
		echo 'Invalid command'
		display_help
		exit 1
		;;
esac

