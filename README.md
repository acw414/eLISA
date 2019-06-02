# README

***Welcome to xxxxx, written by Anna Weir and Sohil Joshi.***

This project primarily uses data from [Environmental DNA](https://www.sciencedirect.com/science/article/pii/S0006320714004443) (eDNA), which is the genetic material that organisms shed into the environment around them, similar to how humans shed hair and skin cells throughout the day. This genetic material provides us insight into the past and present as it identifies all species that have passed through a particular area through analyzing samples of water, soil, sediment etc.   

This process can be done by first collecting samples, extracting and purifying the DNA, and then amplifying it through a technique known as [PCR](https://www.yourgenome.org/facts/what-is-pcr-polymerase-chain-reaction). This method is advantageous as it is more efficient that conducting observations/trapping, and also does a quantitative analysis which aids in population count.   

eDNA can be used to track the spread of invasive species, which are species that have been introduced, either intentionally or unintentionally, to a region outside their natural range and subsequently caused harm to this new habitat. This is a worthwhile field of study as population booms of invasive species could threaten native species, [disrupt ecosystem functions](https://www.environmentalscience.org/invasive-species), and even cause [millions of dollars worth of damage](https://2001-2009.state.gov/g/oes/ocns/inv/cs/2304.htm).   

**Purpose of the program:**

The program is designed to make it convenient for biologist to sort through multiple invasive species datasets to retrieve information. The user will be able to identify which species amongst all those present in their eDNA sample are invasive to the sampled area. Additionally, the program will then list the percentage of species that were invasive for each sample site, as well as text detailing the names of each invasive species and some information about where they’re native to. 

**What the user needs installed and dataset format:**

The user will need to use UCLA's Hoffman2 server to run this program. /name of our program/ will load Python and R modules, and data analysis will use the [originr](https://github.com/ropensci/originr) package. 

This program will take a taxonomy file from an eDNA sample as the input. The file should split species in different rows, and the number of occurrences at each sampling site in the columns. This program will extract the species present at each sample site, compare them to datasets using originr, and determine whether the species are invasive or not in the country **specified in the input**. The program also returns other statistics depending on the parameters included by the user.

**PROJECT TO DO LIST**
  - give our project an 'innovative' name. LISA? Listed Invasive Species Analyser?
    - how about eLISA? e for eDNA and change Analyser to Application? = eDNA List Invasive Species Application
    - how about ISPS - Invasive Species Per Sample
  - ~things the user should know in advance - hoffman/originr (to the readme)~   
  - requirements that the user needs on the bioinformatics end   
  - ~more comments in the code itself~       
  - ~add comments to bit saying you're mporting/loading things~   
  - ~printing an error message if they dont have:~
    - ~the right arguments~   
    - ~if the input is not tab delimited or doesnt use semicolons as delimeters in the last column~
  - ~need to start with 'module load R' before starting the program. include in bash script before loading everything.~    
  - need to create the output file   
  - need to delete the finalsamplecolumn files after the output file finishes - do this in bash script    
  - ~need to remove empty lines from finalsamplecolumn files~    
  - add the code that runs the Rcodes in the Bash script .   
  - ~need to remove empty lines from finalsamplecolumn files~    
  - need a section saying all the requirement for the input file .    
    - say the input file cannot have the string "column" in the filename   
    - say it needs to be a tab-delimited table with semicolons seperating the taxonomic info in the last column    
  - make the readme look nice. add the vingette(??) and the other things listed in the project details   
    - maybe make a flow chart of how the program works idk?   
    
***How the README should be structured, according to https://github.com/pceeb/UCLA_Spring_2019/tree/master/Term_project***          
**The Readme (125 pts)**       

**Introduction:** This section indicates the purpose of the program and provides background and a justification for why the program was created.    
**Program Workflow:** This section provides an operation overview of what the program does. A flowchart or some other diagram might be helpful, but is not required.     
**Dependencies:** To run a program users may need to have dependencies installed. Indicate which dependencies are required for you program.   
**Instructions:** You need to indicate how your program is run.    
**Expected Output:** Describe the files and or directories will be produced by your program.   
**References:** Cite pertinent studies or programs that you used to develop your program(s).   

