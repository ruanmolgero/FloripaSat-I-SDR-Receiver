# Compile gr_modtool blocks
cmake ../
make
sudo make install
sudo ldconfig

# # Compile Hierarchical Blocks
# cd ../../Hierarchical-Blocks/
# printf "\nCompiling Hierarchical Blocks"
# mapfile -t file_names < <(find . -name "*.grc")
# for file in "${file_names[@]}"
# do
#     printf '\nCompiling %s' $file
#     grcc $file
# done
# printf "\n"
