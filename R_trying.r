#install.packages("tidyverse")
#install.packages("originr")

library("tidyverse")
library("originr")

x = "Not in GISD"
invasive = list()

setwd('~/Project_local')
files <- list.files(path=".", pattern="finalsamplecolumn.*.txt", full.names=TRUE, recursive=FALSE)
lapply(files, function(x) {
  t <- read.csv(x, header=TRUE) # load file
  out <- function(t){
    for(species in t){
      #presence <- gisd(species)
      #if(x %in% presence){
        #print("Not in database")
      print(species)
      #}
    }
    
  }
  write.csv(out, "~/Project_local/output.txt", sep="\t", quote=FALSE, row.names=FALSE, col.names=TRUE)
})

#https://stackoverflow.com/questions/14958516/looping-through-all-files-in-directory-in-r-applying-multiple-commands
#https://stats.idre.ucla.edu/r/codefragments/read_multiple/
