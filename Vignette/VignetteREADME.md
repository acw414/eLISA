# Vignette ReadMe

This Vignette directory contains 
- Instructions for how to run a sample dataset (listed below)
- An example eDNA dataset in the format required for eLISA to work - sampleinput_Fish_taxonomy_file.txt
- An example output file - results.csv
- An example of the temporary files created by eLISA - finalsamplecolumn1.txt finalsamplecolumn2.txt  
   - These contain all the species present in each eDNA sample, with repeats and empty lines ommitted 
   - Please note these temporary files are deleted by eLISA and will not be produced in a typical run. They are only included in the Vignette to show the intermediary steps eLISA goes through in file processing.

## Running eLISA with an example dataset   

This document will now walk through the steps for running an example dataset through eLISA. 

1) The user should first **install the [originr package](https://github.com/ropensci/originr)** in R.
   - Log into the UCLA Hoffman2 server and type:
       ```
      module load R
      R
        > install.packages("originr")
       ```
   - The package may take up to 10 minutes to install, please do not close R or the terminal window.
   - Then the user should then close R:
       ```
       quit()
       ```
   - This step can be skipped if the user already has originr installed on their terminal. 
   
2) The user can **clone the eLISA directory to Hoffman2** by typing the following into the command line:
   ```
   git clone https://github.com/acw414/eLISA.git
   ```

3) To run the sample data set the user should **copy** sampleinput_Fish_taxonomy_file.txt from eLISA/Vignette to the main eLISA directory

4) Finally, the user needs to **navigate to the main eLISA directory** and type into the command line:
   ```
   sh eLISA.sh sampleinput_Fish_taxonomy_file.txt
   ```
