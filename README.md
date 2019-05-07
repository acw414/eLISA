# README

Welcome to xxxxx, written by Anna Weir and Sohil Joshi. 

*introduction, background, justificaton for project*

This project primarily uses data from Environmental DNA (eDNA), which is the genetic material that organisms shed into the environment around them, similar to how humans shed hair and skin cells throughout the day. This genetic material provides us insight into the past and present as it identifies all species that have passed through a particular area through analyzing samples of water, soil, sediment etc.   

This process can be done by first collecting samples, extracting and purifying the DNA, and then amplifying it through a technique known as [PCR](https://www.yourgenome.org/facts/what-is-pcr-polymerase-chain-reaction). This method is advantageous as it is more efficient that conducting observations/trapping, and also does a quantitative analysis which aids in population count.   

eDNA can be used to track the spread of invasive species, which are species that have been introduced, either intentionally or unintentionally, to a region outside their natural range and subsequently caused harm to this new habitat. This is a worthwhile field of study as population booms of invasive species could threaten native species, [disrupt ecosystem functions] (https://www.environmentalscience.org/invasive-species), and even cause [millions of dollars worth of damage](https://2001-2009.state.gov/g/oes/ocns/inv/cs/2304.htm).   

Purpose of program:

The program is designed to make it convenient for biologist to sort through multiple invasive species datasets to retrieve information. The user will be able to identify which species amongst all those present in their eDNA sample are invasive to the sampled area. Additionally, the program will then list the percentage of species that were invasive for each sample site, as well as text detailing the names of each invasive species and some information about where they’re native to. 

What user needs installed/dataset:

The user will need to install R - a statistical programming and visualization tool. The user will need to install the originr package. 

This program will take a taxonomy file from an eDNA sample as the input, as well as the country or regional area the samples were collected from. The file should split species in different rows, and the number of occurrences at each sampling site in the columns. This program will extract the species, compare them to multiple datasets using originr, and determine whether the species are invasive or not in the country specified in the input. The program also returns other statistics depending on the parameters included by the user.

```
INSTRUCTIONS FOR README:
The name of the program
Choose a self-explaining name for your project.

The authors of the programs
Name of students in your group

The purpose for writing the program 
Let people know what your program can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. Also, depending on what you are making, it can be a good idea to include screenshots or images. Remember your favorite animal repository!!

What they need to have installed to run the program
However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Do they need R packages? Python Libraries?

How to actually use the program 
The commands to run, how to access the help menu, etc. Show the expected output if you can. It’s helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.
```
