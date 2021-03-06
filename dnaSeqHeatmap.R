#! /usr/bin/Rscript

## Author: Patrick Rynkiewicz
## Description: Visualization of DNA Content via heatmap.
#Author: Patrick Rynkiewicz
# read in input file.
seqs <- read.csv('SeqComparison.csv', header = T)

# clean up data.
rownames(seqs) <- seqs[ , 1]
seq_matrix <- data.matrix(seqs[ , -1]) #make the numbers in the file numeric data type.


# plot heatmap.
png(filename = "heatmap_output.png") #open png file.
heatmap(seq_matrix, Rowv=NA, Colv=NA,  scale="column", margins=c(7,10)) #heatmap plot.
dev.off() 
#close the png file.
