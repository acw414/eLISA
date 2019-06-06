# eLISA

## eDNA List Invasive Species Analyzer    
***Written by Anna Weir (annacxweir@gmail.com) and Sohil Joshi (sohiljoshi.email@gmail.com)***   

This project primarily uses data from [Environmental DNA](https://www.sciencedirect.com/science/article/pii/S0006320714004443) (eDNA), which is the genetic material organisms shed into their surrounding environments, similar to how humans shed hair and skin cells throughout the day. This genetic material can be extracted by collecting samples of sediment or water, purifying DNA reads found in the samples, and then amplifying them through a technique known as [PCR](https://www.yourgenome.org/facts/what-is-pcr-polymerase-chain-reaction).     

eDNA can therefore identify any species that have passed through a particular environment based on the fragments of DNA they leave behind. This is more efficient than typical mark-release-recapture methods, and can provide scientists with quantitative data that can aid in large-scale metapopulation analyses.   

eDNA analysis can also track the spread of invasive species; species which have been introduced, either intentionally or unintentionally, to a region outside their natural range and have subsequently caused harm to this new habitat. This is a worthwhile field of study as population booms of invasive species can [threaten native species](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2745.2009.01480.x), [disrupt ecosystem functions](https://www.environmentalscience.org/invasive-species), and even cause [millions of dollars worth of damage](http://www.seagrant.umn.edu/ais/zebramussels_threaten). However, eDNA analyses can identify hundreds of unique DNA reads per sample, and verifying each unique species in invasive species databases would be monotonous and time-consuming.   

eLISA is designed to aid in this laborious task. The program takes the output of an eDNA analysis, searches through the Global Invasive Species Database, and provides the user with a sample-by-sample breakdown of the region-specific invasive species.  eLISA is meant to make eDNA analysis as convenient as possible, and can identify the invasive species in a table of hundreds in a matter of minutes.   


## Program Workflow 

eLISA is comprised of a Python script (***Python_eLISA.py***), which sorts through the file and extracts species names, and an R script (***R_eLISA.r***), which dermines if the species are invasive and creates the output. These two scripts are run by using the bash masterscript (***eLISA.sh***).

The user provides two inputs: a .txt file containing eDNA sample reads and the country where the samples were collected. eLISA will determine the species present in each sample site, and check them against the [Global Invasive Species Database](http://www.iucngisd.org/gisd/) using the [*gisd(sp)*](https://github.com/ropensci/originr/blob/master/R/gisd.R) function in [**originr**](https://github.com/ropensci/originr). eLISA then outputs a file detailing the region-specific invasive species in each sample. 

![alt text](https://github.com/acw414/eLISA/blob/master/workflow.jpg "Program Workflow")   

**eLISA will list a number of status messages while completing tasks:**
- *Sorting input file* will be shown as eLISA goes through the input file and creates a temporary file per sample
- *Searching species database* will show when eLISA moves onto the R part of the script and searches the Global Invasive Species Database
- *Checking species_name* is a status message from originr, and will show each species as it is checked through the system
- *Finalizing output* means eLISA is almost finished and will delete all temporary files   
  
## Dependencies

eLISA runs best on **UCLA's Hoffman2 Cluster**, and requires the use of **Python**(3 or above) and **R**. If you do not have access to Hoffman2, you can run eLISA on your terminal as long as you have downloaded [Python](https://www.python.org/downloads/) and [R](https://cran.r-project.org/mirrors.html).

**First time users must install** [**originr**](https://github.com/ropensci/originr) in R before running eLISA. This can be done in the command line by typing: 
```
module load R
R
  > install.packages("originr")
```
*Please give the system 10-15 minutes for this installation.* Please do not close your terminal or disconnect from the internet until installation is complete and you see the prompt from R again. Proceed to quit R by typing:
```
quit()
```
You are now ready to run eLISA.

There are a number of **requirements for the input file** that, if not met, could impact eLISA's performance:
- The file must be a .txt file of eDNA sample reads and taxonomic data (see /Vignette/sampleinput_Fish_taxonomy_file.txt for an example)  
- The file must be organized into columns 
- The taxonomic data in the final column must use semicolons (;) to seperate taxonomic ranks  
- The name of the input file cannot have the string "column" in it    


## Instructions 

1) If the user is running eLISA for the first time, they should first **install the originr package** by following the instructions under the **Dependencies** section. Skip this step if originr is already installed.   

2) The user can **clone the eLISA repository to Hoffman2** by typing the following into the command line:
  ```
  git clone https://github.com/acw414/eLISA.git
  ```

3) The user should then **load R** by typing
  ```
  module load R
  ```

4) eLISA will only work if the input file and scripts are all in the same directory. Therefore the user should then **copy their input file into eLISA/Scripts**

5) **To run eLISA**, the user should **navigate into the eLISA/Scripts directory** then type:  
  ```
  sh eLISA.sh inputfile.txt "Country the samples were collected from"
  ```
(where inputfile.txt is the name of the user's own input file)

**Please note:** The user must use the correct name and spelling of the country of choice. **Use quotation marks around the country name** to avoid confusion with names that include spaces. Incorrect spelling will still create *results.csv* but it will show 0% invasive species. Having 0% invasiveness could indicate a spelling error, but your dataset could also have 0 invasive species. 

## Expected Output

eLISA produces a text file named *results.csv* which contains a table. This table has 5 columns - Sample(name of the sample), Count(total species), Invasive(number of invasive species), Percentage(number of invasive species as a percent of total species), and Invasive_Species(list of invasive species). The number of rows in the result depends on the number of samples in the input eDNA file. Here is what *results.csv* looks like in terminal:

![alt text](https://github.com/sohil2710/spring2019_-/blob/master/Screen%20Shot%202019-06-05%20at%2012.08.22%20AM.png)

In order to see the results in a clear and tabular form, we recommend that the user should open results.csv with Mircosoft Excel or a text editor. Right click on the file and select *open with*, followed by your application of choice.

Here is what the file looks like in Excel:

![alt text](https://github.com/sohil2710/spring2019_-/blob/master/Screen%20Shot%202019-06-05%20at%2012.40.38%20AM.png)

**UCLA Hoffman users**: In order to view results.csv with another software like Excel, the user must copy the file to a local folder on their computer before proceeding with the instructions above. Do this by typing:
```
scp c177-xx@hoffman2.idre.ucla.edu:/u/home/class/c177/c177-xx/eLISA/Scripts/results.csv path_to_local_folder
```
Remember to replace the part after 'scp' with your own login and the path to results.csv on Hoffman.

## References

Biomeme. (2018). A Guide to Environmental DNA (eDNA) by Biomeme. Retrieved June 6, 2019, from https://biomeme.com/environmental-dna/

Hejda, M. , Pyšek, P. and Jarošík, V. (2009), Impact of invasive plants on the species richness, diversity and composition of   invaded communities. Journal of Ecology, 97: 393-403. doi:10.1111/j.1365-2745.2009.01480.x

Hill, J. (2015, February 23). Invasive Species: How They Affect the Environment. Retrieved June 6, 2019, from                 https://www.environmentalscience.org/invasive-species

Minnesota Sea Grant. (2017, March 30). Zebra Mussels Threaten Inland Waters. Retrieved June 6, 2019, from   http://www.seagrant.umn.edu/ais/zebramussels_threaten

Python Software Foundation. Python Language Reference, version 3. URL http://www.python.org

R Core Team (2014). R: A language and environment for statistical computing. R Foundation for Statistical Computing, Vienna,     Austria. URL http://www.R-project.org/.

Scott Chamberlain and Ignasi Bartomeus (2018). originr: Fetch Species  
  Origin Data from the Web. R package version 0.3.0.
  https://CRAN.R-project.org/package=originr

Thomsen, P. F. (2014, December 18). Environmental DNA – An emerging tool in conservation for monitoring past and present biodiversity. Retrieved June 6, 2019, from https://www.sciencedirect.com/science/article/pii/S0006320714004443

## Acknowledgements

We would like to thank **Dr. Emily Curd and Daniel Chavez at UCLA** for the inspiration for this project. Their continued support and guidance over 10 weeks introduced us to bioinformatics and made this project possible.


_______________

**PROJECT TO DO LIST**   
  - add more comments in the code itself 
  - make our DOI + include how to cite us 
  - see if we can find a list of the countries accepted by gsid
