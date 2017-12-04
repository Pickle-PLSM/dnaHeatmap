
# Fetch command line arguments
myArgs <- commandArgs(trailingOnly = TRUE)

# Convert to numerics
nums = as.numeric(myArgs)

# cat will write the result to the stdout stream
cat(nums[1])

pdf(file="myplot.pdf")

vector <- c(1, 6, 2, 1)
barplot(vector, names.arg=c("A","T","C","G"))

#graph(nums[1], nums[2], nums[3], nums[4])

#graph <- function(ACount, TCount, CCount, GCount) {
#  vector <- c(ACount, TCount, CCount, GCount)
#  barplot(vector, names.arg=c("A","T","C","G"))
#}

