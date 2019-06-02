#install.packages("tidyverse")
#install.packages("originr")

library("tidyverse")
library("originr")

sink('output.txt')
setwd('~/Project_local') #change this to current directory
files <- list.files(path=".", pattern="finalsamplecolumn.*.txt", full.names=TRUE, recursive=FALSE)
lapply(files, function(x) {
  t <- read.csv(x, header=TRUE) # load file
  t <- t[[1]]
  print('New file')
  out <- for(species in t){
    presence <- gisd(species)
    print(presence)
  }
})
sink()
#invasive_per_file = (number of invasive species/number of total species)*100
#need to produce a file that has a table with name of sample file, %invasive, print list invasive, and native_range
