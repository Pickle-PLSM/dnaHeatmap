# Author: Sofie Christie

# Fetch command line arguments
#myArgs <- commandArgs(trailingOnly = TRUE)

# Convert to numerics
# nums = as.numeric(myArgs)

png(file="plot.png")

#df <- read.csv(text =
#"File,A,T,C,G
#Seq1.txt,214,214,210,189
#Seq2.txt,120,120,130,67
#Seq3.txt,119,118,58,42
#Seq4.txt,95,96,90,180", header = TRUE)

df <- read.csv("SeqComparison.csv", header = TRUE)

library(ggplot2)
library(reshape2)

df <- melt(df, id = 'File')
ggplot(
   data = df,
   aes(
      y = value,
      x = File,
      group = variable,
      shape = variable,
      fill = variable
   )
) +
geom_bar(stat = "identity") + labs(y="Count", fill="Base", title="ATGC Content Relative to Different Sequences")
