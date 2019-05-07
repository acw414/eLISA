# README

***Welcome to xxxxx, written by Anna Weir and Sohil Joshi.***

This project primarily uses data from [Environmental DNA](https://www.sciencedirect.com/science/article/pii/S0006320714004443) (eDNA), which is the genetic material that organisms shed into the environment around them, similar to how humans shed hair and skin cells throughout the day. This genetic material provides us insight into the past and present as it identifies all species that have passed through a particular area through analyzing samples of water, soil, sediment etc.   

This process can be done by first collecting samples, extracting and purifying the DNA, and then amplifying it through a technique known as [PCR](https://www.yourgenome.org/facts/what-is-pcr-polymerase-chain-reaction). This method is advantageous as it is more efficient that conducting observations/trapping, and also does a quantitative analysis which aids in population count.   

eDNA can be used to track the spread of invasive species, which are species that have been introduced, either intentionally or unintentionally, to a region outside their natural range and subsequently caused harm to this new habitat. This is a worthwhile field of study as population booms of invasive species could threaten native species, [disrupt ecosystem functions](https://www.environmentalscience.org/invasive-species), and even cause [millions of dollars worth of damage](https://2001-2009.state.gov/g/oes/ocns/inv/cs/2304.htm).   

**Purpose of program:**

The program is designed to make it convenient for biologist to sort through multiple invasive species datasets to retrieve information. The user will be able to identify which species amongst all those present in their eDNA sample are invasive to the sampled area. Additionally, the program will then list the percentage of species that were invasive for each sample site, as well as text detailing the names of each invasive species and some information about where they’re native to. 

**What the user needs installed and dataset format:**

The user will need to install R - a statistical programming and visualization tool. The user will need to install the [originr](https://github.com/ropensci/originr) package. 

This program will take a taxonomy file from an eDNA sample as the input, as well as the country or regional area the samples were collected from. The file should split species in different rows, and the number of occurrences at each sampling site in the columns. This program will extract the species, compare them to multiple datasets using originr, and determine whether the species are invasive or not in the country specified in the input. The program also returns other statistics depending on the parameters included by the user.


