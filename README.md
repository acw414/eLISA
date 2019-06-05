# eLISA

## eDNA List Invasive Species Analyzer    
***Written by Anna Weir (annacxweir@gmail.com) and Sohil Joshi (sohiljoshi.email@gmail.com)***   

This project primarily uses data from [Environmental DNA](https://www.sciencedirect.com/science/article/pii/S0006320714004443) (eDNA), which is the genetic material organisms shed into their surrounding environments, similar to how humans shed hair and skin cells throughout the day. This genetic material can be extracted by collecting samples of sediment or water, purifying DNA reads found in the samples, and then amplifying them through a technique known as [PCR](https://www.yourgenome.org/facts/what-is-pcr-polymerase-chain-reaction).     

eDNA can therefore identify any species that have passed through a particular environment based on the fragments of DNA they leave behind. This is more efficient than typical mark-release-recapture methods, and can provide scientists with quantitative data that can aid in large-scale metapopulation analyses.   

eDNA analysis can also track the spread of invasive species; species which have been introduced, either intentionally or unintentionally, to a region outside their natural range and have subsequently caused harm to this new habitat. This is a worthwhile field of study as population booms of invasive species could threaten native species, [disrupt ecosystem functions](https://www.environmentalscience.org/invasive-species), and even cause [millions of dollars worth of damage](https://2001-2009.state.gov/g/oes/ocns/inv/cs/2304.htm). However, eDNA analyses can identify hundreds of unique DNA reads per sample, and verifying each unique species in invasive species databases would be monotonous and time-consuming.   

eLISA is designed to aid in this laborious task. The program takes the output of an eDNA analysis, searches through the Global Invasive Species Database, and provides the user with a sample-by-sample breakdown of the identified invasive species. The program is only set to check for species that are invasive within the US inland range. The authors are currently working on adding an option for the user to chose which country the program will check invasiveness for. eLISA is meant to make eDNA analysis as convenient as possible, and can identify the invasive species in a table of hundreds in a matter of minutes.   


## Program Workflow 

The user provides a .txt file containing eDNA sample reads and taxonomic data as an input, and eLISA will extract the species present at each sample site, check them against invasive species databases using originr, and output a file detailing the invasive species in each sample.  

![alt text](https://github.com/acw414/eLISA/blob/master/project_workflow.jpg "Program Workflow")   

**eLISA will list a number of status messages while completing tasks:**
- *Sorting input file* will be shown as eLISA goes through the input file and creates a temporary file per sample
- *Searching species database* will show when eLISA moves onto the R part of the script and searches the Global Invasive Species Database
- *Checking <species name>* is a status message from originr, and will show each species as it is checked through the system
- *Finalizing output* means eLISA is almost finished and will delete all temporary files   
  
## Dependencies

eLISA requires the use of Python(3 and above) and R. If your computer or server does not have [Python](https://www.python.org/downloads/) and [R](https://cran.r-project.org/mirrors.html) dowloaded, then please click the link embeded. 

Additionally, eLISA uses the R package - [originr](https://github.com/ropensci/originr) to query the [Global Invasive Species Database](http://www.iucngisd.org/gisd/). This program only uses the [*gisd(sp)*](https://github.com/ropensci/originr/blob/master/R/gisd.R) function for access to the aformentioned database.

**First time users** must install this package in R. Go to your command line and type 'R' to load R. Once you are given the prompt type:
```
install.packages("originr")
```
Please give the system 10-15 minutes for this install. Please do not close your terminal or disconnect from the internet until the installation is complete and you see the prompt from R again. Proceed to quit R by typing:
```
quit()
```
**UCLA Hoffman users only** : Python and R are already installed on the server. After retrieving a compute node, the user must type the following in order to load R:
```
module load R
```
Please follow the instructions above in order to install the originr package and then quit R. 


## Instructions 

1) If the user is **running eLISA for the first time**, they should start by installing the originr package by following the instructions under the **Dependencies** section. Skip this step if originr is already installed.   

2) The user can **clone the eLISA repository to Hoffman2** by typing:
```
git clone https://github.com/acw414/eLISA.git
```
into Hoffman2. This should make a copy of this repository. 

3) **To run eLISA** the user should move their input file into the eLISA/Scripts directory, navigate into this directory, and type:  
```
sh eLISA.sh inputfile.txt
```
where inputfile.txt is the name of the user's own input file.

There are a number of **requirements for the input file** that, if not met, could impact eLISA's performance:
- The file must be a .txt file of eDNA sample reads and taxonomic data (see /Vignette/sampleinput_Fish_taxonomy_file.txt for an example)  
- The file must be organized into columns 
- The taxonomic data in the final column must use semicolons (;) to seperate taxonomic ranks  
- The name of the input file cannot have the string "column" in it   


## Expected Output

eLISA produces a text file named *results.csv* which contains a table. This table has 5 columns - Sample(name of the sample), Count(total species), Invasive(# of invasive species), Percentage(% of invasive species), and Invasive_Species(list of invasive species). The number of rows in the result depends on the number of samples in the input eDNA file. Here is what *results.csv* looks like in terminal:

![alt text](https://github.com/sohil2710/spring2019_-/blob/master/Screen%20Shot%202019-06-05%20at%2012.08.22%20AM.png)

In order to see the results in a clear and tabular form, we recommend that the user should open results.csv with Mircosoft Excel or a text editor. Right click on it and select *open with*, followed by your application of choice.

Here is what the file looks like in Excel:

![alt text](https://github.com/sohil2710/spring2019_-/blob/master/Screen%20Shot%202019-06-05%20at%2012.40.38%20AM.png)

**UCLA Hoffman users**: In order to view the file in with another software like Excel, the user must copy the file on to their computer before proceeding with the instructions above. Remember to do this by typing:
```
scp c177-23@hoffman2.idre.ucla.edu:/u/home/class/c177/c177-xx/eLISA/results.csv *path to location on your computer*
```
Remember to replace the part after 'scp' with your own login and the path to results on Hoffman.



## References

Scott Chamberlain and Ignasi Bartomeus (2018). originr: Fetch Species  
  Origin Data from the Web. R package version 0.3.0.
  https://CRAN.R-project.org/package=originr






_______________

**PROJECT TO DO LIST**   
  - add more comments in the code itself 
  - make our DOI + include how to cite us 

