mkdir output;cp -r input/* output/;for file in output/*/*.pdf; do pdftotext "$file" "$file.txt"; done;for file in output/*/*.pdf;do rm "$file"; done;