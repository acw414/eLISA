#install.packages("originr")

#need to comment all over this code
#currently works for checking if invasive in "united states" - line 19


library("originr")

files <- list.files(path=".", pattern="finalsamplecolumn.*.txt", full.names=TRUE, recursive=FALSE)

results <- data.frame()

for (file in files){
    t <- read.csv(file, header=TRUE, stringsAsFactors = F)
    invasive <- 0
    invasive_species <- c()
    for (species in t[,1]){
      presence <- gisd(species)
      if (is.null(presence[[1]]$status)){
        if ("united states" %in% presence[[1]]$alien_range){
          invasive <- invasive + 1
          invasive_species <- c(invasive_species, presence[[1]]$species)
        }
      }
    }
    current <- data.frame(sample = colnames(t)[1], count = nrow(t), 
                          invasive = invasive, percentage =  (invasive/ nrow(t)*100),
                          invasive_species = paste(invasive_species, collapse = ', '))
    results <- rbind(results, current)
}

summary <- data.frame(sample='total', count = sum(results$count), invasive = sum(results$invasive),
                      percentage = (sum(results$invasive)/sum(results$count))*100,
                      invasive_species = '')
results <- rbind(results, summary)

write.csv(results, 'results.csv', row.names = F)
