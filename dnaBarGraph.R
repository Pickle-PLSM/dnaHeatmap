# Author: Sofie Christie
# Description: Create a stacked bar graph based off a csv created in python

# print graph to png
png(file="bargraph.png")

# read in the csv
df <- read.csv("SeqComparison.csv", header = TRUE)

# import the ggplot2 library for better graphing capabilities
library(ggplot2)
# import the reshape2 library to better format the data
library(reshape2)

df <- melt(df, id = 'File')
ggplot(
   data = df,
   aes(
      # input parameters
      y = value,
      x = File,
      group = variable,
      shape = variable,
      fill = variable
   )
) +
# add graph and labels
geom_bar(stat = "identity") + labs(y="Count", fill="Base", title="ATGC Content Relative to Different Sequences")
