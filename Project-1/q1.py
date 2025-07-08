#will print the string up to the position selected, then will concatnate with the new character they we select and then print of the rest of the string from that postion.
replace_ch_in_pos = lambda word, char, posi: word[:posi] + char + word[posi +1:]


