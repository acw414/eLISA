# README

***Welcome to xxxxx, written by Anna Weir and Sohil Joshi.***

This project primarily uses data from [Environmental DNA](https://www.sciencedirect.com/science/article/pii/S0006320714004443) (eDNA), which is the genetic material that organisms shed into the environment around them, similar to how humans shed hair and skin cells throughout the day. This genetic material provides us insight into the past and present as it identifies all species that have passed through a particular area through analyzing samples of water, soil, sediment etc.   

This process can be done by first collecting samples, extracting and purifying the DNA, and then amplifying it through a technique known as [PCR](https://www.yourgenome.org/facts/what-is-pcr-polymerase-chain-reaction). This method is advantageous as it is more efficient that conducting observations/trapping, and also does a quantitative analysis which aids in population count.   

eDNA can be used to track the spread of invasive species, which are species that have been introduced, either intentionally or unintentionally, to a region outside their natural range and subsequently caused harm to this new habitat. This is a worthwhile field of study as population booms of invasive species could threaten native species, [disrupt ecosystem functions](https://www.environmentalscience.org/invasive-species), and even cause [millions of dollars worth of damage](https://2001-2009.state.gov/g/oes/ocns/inv/cs/2304.htm).   

**Purpose of the program:**

The program is designed to make it convenient for biologist to sort through multiple invasive species datasets to retrieve information. The user will be able to identify which species amongst all those present in their eDNA sample are invasive to the sampled area. Additionally, the program will then list the percentage of species that were invasive for each sample site, as well as text detailing the names of each invasive species and some information about where they’re native to. 

**What the user needs installed and dataset format:**

The user will need to install R - a statistical programming and visualization tool. The user will need to install the [originr](https://github.com/ropensci/originr) package. The user will need to use UCLA's Hoffman server to perform computations. Once logged in, the user will need to load Python and R modules. 

This program will take a taxonomy file from an eDNA sample as the input, as well as the country or regional area the samples were collected from. The file should split species in different rows, and the number of occurrences at each sampling site in the columns. This program will extract the species, compare them to multiple datasets using originr, and determine whether the species are invasive or not in the country specified in the input. The program also returns other statistics depending on the parameters included by the user.

***THINGS TO ADD***
  - give our project an 'innovative' name. LISA? Listed Invasive Species Analyser?
  - *things the user should know in advance - hoffman/originr (to the readme) - Done*  
  - format of the file - each sequence entry must be on a new line   
  - requirements that the user needs on the bioinformatics end   
  - *more comments in the code itself*    
  - add comments to bit saying you're mporting/loading things   
  - printing an error message if they dont have:
    - the right arguments   
    - if the input is not tab delimited or doesnt use semicolons as delimeters in the last column
    
to skip the 1st line  
do an if statement, if line not in uniq 1 and line >1 (or zero): do   
do an if statmenet   
if line = 0, split line by tabs, and write the 1st element   
else, (if not the 1st line), do the repeating thing    
print the len of every single line. see how it works   
use header as a reference - for i in len(elementds in header)   
make a count of all species  + make the list of the unusable species
