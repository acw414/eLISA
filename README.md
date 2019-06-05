# eLISA

## eDNA List Invasive Species Analyzer    
***Written by Anna Weir (annacxweir@gmail.com) and Sohil Joshi (sohiljoshi.email@gmail.com)***   

This project primarily uses data from [Environmental DNA](https://www.sciencedirect.com/science/article/pii/S0006320714004443) (eDNA), which is the genetic material organisms shed into their surrounding environments, similar to how humans shed hair and skin cells throughout the day. This genetic material can be extracted by collecting samples of sediment or water, purifying DNA reads found in the samples, and then amplifying them through a technique known as [PCR](https://www.yourgenome.org/facts/what-is-pcr-polymerase-chain-reaction).     

eDNA can therefore identify any species that have passed through a particular environment based on the fragments of DNA they leave behind. This is more efficient than typical mark-release-recapture methods, and can provide scientists with quantitative data that can aid in large-scale metapopulation analyses.   

eDNA analysis can also track the spread of invasive species; species which have been introduced, either intentionally or unintentionally, to a region outside their natural range and have subsequently caused harm to this new habitat. This is a worthwhile field of study as population booms of invasive species could threaten native species, [disrupt ecosystem functions](https://www.environmentalscience.org/invasive-species), and even cause [millions of dollars worth of damage](https://2001-2009.state.gov/g/oes/ocns/inv/cs/2304.htm). However, eDNA analyses can identify hundreds of unique DNA reads per sample, and verifying each unique species in invasive species databases would be monotonous and time-consuming.   

eLISA is designed to aid in this laborious task. The program takes the output of an eDNA analysis, searches through an online invasive species database, and provides the user with a sample-by-sample breakdown of the identified invasive species. eLISA   is meant to make eDNA analysis as convenient as possible, and can identify the invasive species in a table of hundreds in a matter of minutes.   


### Program Workflow 

The user provides a .txt file containing eDNA sample reads and taxonomic data as an input, and eLISA will extract the species present at each sample site, check them against invasive species databases using originr, and output a file detailing the invasive species in each sample. The program is only set to check for species that are invasive within the US inland range. 

![alt text](https://github.com/acw414/eLISA/blob/master/project_workflow.jpg "Program Workflow")   

**eLISA will list a number of status messages while completing tasks:**
- *Sorting input file* will be shown as eLISA goes through the input file and creates a temporary file per sample
- *Searching species database* will show when eLISA moves onto the R part of the script and searches the Global Invasive Species Database
- *Checking <species name>* is a status message from originr, and will show each species as it is checked through the system
- *Finalizing output* means eLISA is almost finished and will delete all temporary files   
  
### Dependencies

The user will need to use UCLA's Hoffman2 Cluster to run this program. 
eLISA will load Python and R modules, and data analysis will use the [originr](https://github.com/ropensci/originr) package. 

### Instructions 

1) If the user is **running eLISA for the first time**, they should start by installing the originr package. Skip this step if originr is already installed.   

2) The user can **clone the eLISA repository to Hoffman2** by typing:
```
git clone https://github.com/acw414/eLISA.git
```
into Hoffman2. This should make a copy of this repository. 

3) **To run eLISA** the user should move their input file into the eLISA directory, navigate into the directory, and type:  
```
sh eLISA.sh inputfile.txt
```
where inputfile.txt is the name of the user's own input file.

There are a number of **requirements for the input file** that, if not met, could impact eLISA's performance:
- The file must be a .txt file of eDNA sample reads and taxonomic data (see /Vignette/sampleinput_Fish_taxonomy_file.txt for an example)  
- The file must be organized into columns 
- The taxonomic data in the final column must use semicolons (;) to seperate taxonomic ranks  
- The name of the input file cannot have the string "column" in it   


### Expected output
*Describe the files and or directories will be produced by your program.*   
what the table looks like. how the user should view it   

### References
*Describe the files and or directories will be produced by your program.*  

Scott Chamberlain and Ignasi Bartomeus (2018). originr: Fetch Species  
  Origin Data from the Web. R package version 0.3.0.
  https://CRAN.R-project.org/package=originr

_______________

**PROJECT TO DO LIST**   
  - EXPECTED OUTPUT section
  - DEPENDENCIES: requirements that the user needs on the bioinformatics end     
    - must be on UCLA's Hoffman2   
    - must have originr installed beforehand on R (+ instructions of how to install it on Hoffman2)    
    - say what part of origin r we are using : which functions/features. which databases do they analyze? what info do these databases have?
    - can be the same as the readme bits in the vignette?            
  - say this only works for US within inland range 
  - add more comments in the code itself 
  - make our DOI + include how to cite us 
    
   
***How the README should be structured***            
rubric : https://github.com/pceeb/UCLA_Spring_2019/blob/master/Term_project/Rubric.md    

**The Readme (125 pts)**       

**Introduction:** This section indicates the purpose of the program and provides background and a justification for why the program was created.    
**Program Workflow:** This section provides an operation overview of what the program does. A flowchart or some other diagram might be helpful, but is not required.     
**Dependencies:** To run a program users may need to have dependencies installed. Indicate which dependencies are required for you program.   
**Instructions:** You need to indicate how your program is run.    
**Expected Output:** Describe the files and or directories will be produced by your program.   
**References:** Cite pertinent studies or programs that you used to develop your program(s).   

