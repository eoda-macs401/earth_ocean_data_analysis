# Installing Jupyter Lab
## Installation instructions for Anaconda (or miniConda) on your machine:
## MACS497 (MACS401)

*Content modified from Greg Waite’s 2019 Cider workshop*  
This document outlines instructions for installing Anaconda package manager for Python 3.  Use this document to help you get started if you’re using your personal machine for class work.  If you would prefer to use a University Computer Lab, you should not need to do any installation, as long as Jupyter Lab has been installed.  

## Step 1 – Make some choices and install: 

### Chioce \#1:  Anaconda (3Gb) or miniconda (1Gb):

- If you have room, install the full Anaconda – it includes lots of useful features (and some that may be unnecessary).
- If you have any issues with hard drive space on your computer, miniconda has everything we’ll need for this class, or can have everything with a little more setup. 
- Either way, this python installation will be separate from your computers already-installed version of Python (if it has one) and shouldn’t corrupt anything on your system. 

### Choice \#2: find your operating system & follow instructions to install:
### Windows
*Install Anaconda From Here: [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)*  
1. Follow link and scroll down to the bottom to the Anaconda Installers section and find the download link. The current version is 3.8 and you’ll want 64 Bit. Download this version and double click on the installer once it is finished downloading. 
2. Install to your C: drive (should be the default)
#### From here, start Juypter Lab
6. You can open an **Anaconda Prompt** from the start menu to open what is essentially a terminal window. 
7. Install Jupyter Lab by typing the following into the terminal after the *prompt* (NOTE - do not type the "$", it is symbolizing the *prompt* in the following guide): 

```
$ conda install -c conda-forge jupyterlab
```

8. Follow the prompts to complete the installation. We may do this again after we discuss environments - stay tuned. 
9. Once the installation completes - start Jupyter Lab by typing (do not type the "$"): 

```
$ jupyter lab
```


### Mac (or Linux if you have one!)
*Install Anaconda From Here: [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)*  
1. Follow link and scroll down to the bottom to the Anaconda Installers section and find the download link. The current version is 3.8 and you’ll want 64 Bit. Choose the Anacnoda Graphical Installer. 
2. Once the installer (.pkg) has finished downloading (probably to your Downloads folder), double click to start the installation. 
3. Make sure it installs on your primary hard-drive (not an external hard-drive, etc.)
4. To see if your system is configured correctly, find your Terminal application and open it.  You can search for terminal within in Finder if you don’t know where it is. When Terminal opens, type the following (NOTE - do not type the "$", it is symbolizing the *prompt* in the following guide): 

```
$ which conda
```

If you get a response other than “not found” you’re good to go.  If you get a “not found” response, get in touch with a classmate or Emily and she’ll help troublshoot (this isn’t uncommon!). 

From here, install Juypter Lab

7. Install Jupyter Lab by typing the following into the terminal after the *prompt* (NOTE - do not type the "$", it is symbolizing the *prompt* in the following guide): 

```
$ conda install -c conda-forge jupyterlab
```

8. Follow the prompts to complete the installation. We may do this again after we discuss environments - stay tuned. 
9. Once the installation completes - start Jupyter Lab by typing the following into terminal (do not type the "$"): 

```
$ jupyter lab
```

## NEXT STEPS

•	BUT: While you’re at it, make a folder to work from for the quarter!! (or in otherwords, set up a good system for organizing your work)
o	If you have your WWU OneDrive automatically mounting to your computer (HIGHLY RECOMMENDED), that may be a good option.  Instructions here:
https://atus.wwu.edu/kb/sync-your-onedrive-your-computer

This is also a great option if you’re using the University computer lab, as your OneDrive account will automatically mount on your lab computer when you log in, and will be accessible from any computer or from your home. 

o	Alternatively (Not highly recommended)  find a place (not the Desktop preferably) that you can easily navigate to.  For example, choose a location in your home directory, such as:
/Users/emily/Classes/2021Winter/Geohaz/Week1 would keep you really organized (as long as you can remember how to get there).  Remember to periodically back up your harddrive! 




•	BUT: While you’re at it, make a folder to work from for the quarter!! (or in otherwords, set up a good system for organizing your work)
o	If you have your WWU OneDrive automatically mounting to your computer (HIGHLY RECOMMENDED), that may be a good option.  Instructions here:
https://atus.wwu.edu/kb/sync-your-onedrive-your-computer

This is also a great option if you’re using the University computer lab, as your OneDrive account will automatically mount on your lab computer when you log in, and will be accessible from any computer or from your home. 

o	Alternatively (Not highly recommended) find a place (not the Desktop preferably) that you can easily navigate to.  For example, choose a location on the C: drive or something similar, and make folders that will allow you to stay organized.  A file structure like C: > Users > you > 2021Winter > Geohaz > Week1  would keep you really organized (as long as you can remember how to get there).  Remember to periodically back up your harddrive!