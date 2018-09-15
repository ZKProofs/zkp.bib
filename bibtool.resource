input {zkp.bib}
output.file = zkp.bib
rewrite.rule {"^\"\([^#]*\)\"$" "{\1}"}
sort = on
sort.format = {%d(year) # %N(key)}
sort.reverse = off