#install.packages("originr")

#need to comment all over this code

library("originr")

files <- list.files(path=".", pattern="finalsamplecolumn.*.txt", full.names=TRUE, recursive=FALSE)

results <- data.frame()

for (file in files){
    mydata <- read.csv(file, header=TRUE, stringsAsFactors = F)
    invasive <- 0
    invasive_species <- c()
    for (species in mydata[,1]){
      presence <- gisd(species)
      if (is.null(presence[[1]]$status)){
        if ("united states" %in% presence[[1]]$alien_range){
          invasive <- invasive + 1
          invasive_species <- c(invasive_species, presence[[1]]$species)
        }
      }
    }
    current <- data.frame(sample = colnames(mydata)[1], count = nrow(mydata), 
                          invasive = invasive, percentage =  invasive/ nrow(mydata),
                          invasive_species = paste(invasive_species, collapse = ', '))
    results <- rbind(results, current)
}

summary <- data.frame(sample='total', count = sum(results$count), invasive = sum(results$invasive),
                      percentage = sum(results$invasive)/sum(results$count),
                      invasive_species = '')
results <- rbind(results, summary)

write.csv(results, 'results.csv', row.names = F)
