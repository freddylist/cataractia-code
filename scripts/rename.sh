DIR=$(dirname $0)/..

INPUT="$DIR/patched"
OUTPUT="$DIR/final"

REPLACEMENTS='Cascadia Code PL/Cataractia Code,cascadia code pl/cataractia code,CascadiaCodePL/CataractiaCode,cascadiacodepl/cataractiacode'

#REPLACEMENTS='Cascadia Code PL/Cataractia Code Frozen,cascadia code pl/cataractia code frozen,CascadiaCodePL/CataractiaCodeFrozen,cascadiacodepl/cataractiacodefrozen'

COPYRIGHT='© 2021 Frederik List'
LICENSE="$DIR/LICENSE"

IFS=',' read -ra replacements <<< "$REPLACEMENTS"

rename () {
	file="$1"
	output="$2"

	file_name=$(basename "$file")

	for replacement in "${replacements[@]}"
	do
		file_name=$(echo "$file_name" | sed s/"$replacement"/g)
	done

	echo $file_name

	fontforge -quiet -script "$DIR/rename.py" -r "$REPLACEMENTS" -copyright "$COPYRIGHT" -license "$LICENSE" --out "$output/$file_name" "$file"
}

for file in $INPUT/*
do
	if [ -f "$file" ]
	then
		rename "$file" "$OUTPUT" &
	fi
done

wait