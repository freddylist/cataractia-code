DIR=$(dirname $0)/..

ARGS=(-f 'calt,ss01,ss02,ss19,ss20,zero')

bake () {
	file=$1
	output=$2

	filename=$(basename "$file")

	pyftfeatfreeze "${ARGS[@]}" "$file" "$output/$filename"
}

recurse () {
	input=$1
	output=$2

	for file in $input/*
	do
		if [ -f "$file" ]
		then
			bake "$file" "$output" &
		else
			folder_name=$(basename "$file")

			recurse "$file" "$output/$folder_name"
		fi
	done

	wait
}

recurse "$DIR/original" "$DIR/frozen"