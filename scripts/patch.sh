DIR=$(dirname $0)/..

ARGS=(-c -w --careful)

patch () {
	file="$1"
	output="$2"

	fontforge -quiet -script "$DIR/font-patcher.py" "${ARGS[@]}" --no-progressbars --shutup --glyphdir '../glyphs/' --out "$output" "$file"
}

recurse () {
	input=$1
	output=$2

	for file in $input/*
	do
		if [ -f "$file" ]
		then
			patch $file $output &
		else
			folder_name=$(basename "$file")

			recurse "$file" "$output/$folder_name"
		fi
	done

	wait
}

recurse "$DIR/original" "$DIR/patched" &
recurse "$DIR/frozen" "$DIR/patched/frozen"