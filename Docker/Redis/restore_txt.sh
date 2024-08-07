#! bin/bash
usage() {
	echo "Usage: $0  <rdb-file> -h <host> -p <port> -a <password>"
	exit 1
}

# check arguments
if ["$#" -ne 8 ]; then
	usage
fi

while getopts ":f:h:p:a:" opt; do
	case ${opt} in
		f)
			rdb_file=$OPTARG
			;;
		h)
			host=$OPTARG
			;;
		p)
			port=$OPTARG
			;;
		a)
			password=$OPTARG
			;;
		\?)
			echo "Invalid option: -$OPTARG" >&2
			usage
			;;
		:)
			echo "Option -$OPTARG requires an argument." >&2
			usage
			;;
	esac
done

if [ -z "$rdb_file" ] || [ -z "$host" ] || [ -z "$port" ] || [ -z "$password" ]; then
	usage
fi

cat "$rdb_file" | redis-cli -h "$host" -p "$port" --pipe -a "$password"
