# Author: Sofie Christie

# Fetch command line arguments
myArgs <- commandArgs(trailingOnly = TRUE)

# Convert to numerics
nums = as.numeric(myArgs)

pdf(file="plot.pdf")

#vector1 <- c(nums[1], nums[2], nums[3], nums[4])
#barplot(vector1, names.arg=c("A","T","C","G"))

#vector2 <- c(2, 8, 18, 1)
#barplot(vector2, names.arg=c("A","T","C","G"))

graph <- function(ACount, TCount, CCount, GCount) {
  vector <- c(ACount, TCount, CCount, GCount)
  barplot(vector, names.arg=c("A","T","C","G"), col=rainbow(4), main="ATCG Content", xlab="Nucleotide Bases", ylab="Count", xpd=FALSE, ylim=c(0,max(nums)+5))
}

graph(nums[1], nums[2], nums[3], nums[4])
graph(1, 2, 5, 3)
