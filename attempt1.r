#!/usr/bin/env Rscript
#usage- Rscript --vanilla finalRcode.R
#install.packages("tidyverse")
#install.packages("originr")

library("tidyverse")
library("originr")

x = "Not in GISD"


setwd('~/Project_local')

filenames <- list.files(path = ".",pattern="finalsamplecolumn.*.txt") #finds required species files
for( i in (filenames) ) #creates for-loop for those files
{
  file = read.csv(i,header=T)
  filevector = file[[1]]
  charvector = as.character(filevector)
  total = length(filevector)
  for(element in charvector){
    presence <- gisd(element)
    if(x %in% presence){
      print("Not in database")
    }
     
    #else{ 
    #  for (i in seq(1,total)){
      
    #  invasive[i] = 1 + element
    #}
    #}
  }
}

invasive = list()
print(invasive)

percent_invasive = ((length(invasive))/total)*100  
cat(percent_invasive, 'percent of species in this sample are invasive') 

for(y in invasive){
  cat('species is found in', native_range)
}
#need to produce a file that has a table with name of sample file, %invasive, print list invasive, and native_range