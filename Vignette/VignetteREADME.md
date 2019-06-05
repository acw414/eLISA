# Vignette ReadMe

**Running eLISA with example datasets**   

This document will walk through a sample running of eLISA. 

Steps for running the program:  
1) The user should first install the [originr package](https://github.com/ropensci/originr) in R.
   - Log into the UCLA Hoffman2 server and type:
       ```
      module load R
      R
        > install.packages("originr")
       ```
   - The package may take up to 10 minutes to install, please do not close R or the terminal window.
   - After the user has installed originr once, they do not need to do so again and can skip this step.
   - Then the user should then close R:
       ```
       quit()
       ```
2) The user can clone the eLISA repository to Hoffman2 by typing the following into the command line:
   ```
   git clone https://github.com/acw414/eLISA.git
   ```

3) The user should **copy sampleinput_Fish_taxonomy_file.txt to the main eLISA directory**

4) Finally, the user needs to **navigate to the main eLISA directory** and type into the command line:
   ```
   sh eLISA.sh sampleinput_Fish_taxonomy_file.txt
   ```
