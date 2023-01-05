# Installing JupyterLab
## Installation instructions for Anaconda (or miniConda) on your machine:
## MACS401

*Content modified from Greg Waite’s 2019 Cider workshop:*  
This document outlines instructions for installing Anaconda package manager for Python 3.  Use this document to help you get started if you’re using your personal machine for class work.  If you would prefer to use a University laptop available in IS410, that is also an option, and installation should be simular to what is outlined below for Windows installation.

## Step 1 – Make some choices and install: 

### Chioce \#1:  Anaconda (3Gb) or miniconda (1Gb):

- If you have room, install the full Anaconda – it includes lots of useful features (and some that may be unnecessary).
- If you have any issues with hard drive space on your computer, miniconda has everything we’ll need for this class, or can have everything with a little more setup. 
- Either way, this python installation will be separate from your computers already-installed version of Python (if it has one) and shouldn’t corrupt anything on your system. 

### Choice \#2: find your operating system & follow instructions to install:
### Windows
*Install Anaconda From Here: [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)*  
1. Follow link and scroll down to the bottom to the **Anaconda Installers** section and find the download link. You’ll want 64 Bit. Download this version and double click on the installer once it is finished downloading. 
2. Install to your C: drive (should be the default)
#### From here, install JuypterLab
3. You can open an **Anaconda Prompt** from the start menu to open what is essentially a terminal window. 
4. Install Jupyter Lab by typing the following into the terminal after the *prompt* (NOTE - do not type the "$", it is symbolizing the *prompt* in the following guide): 

```
$ conda install -c conda-forge jupyterlab
```

5. Follow the prompts to complete the installation. We may do this again after we discuss environments - stay tuned. 
6. Once the installation completes - start Jupyter Lab by typing (do not type the "$") into the terminal: 

```
$ jupyter lab
```
7. This will open up a Jupyter Lab session in a browser.  Follow the guide here: to start to familiarize yourself with the functions within Jupyter Lab. 
8. Moving on to excercises like the Unix Tutorial - you will want to use the terminal, accessed within Jupyter Lab to access your computers directory structure, etc. 

### Mac (or Linux if you have one!)
*Install Anaconda From Here: [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)*  
1. Follow link and scroll down to the bottom to the **Anaconda Installers** section and find the download link. You’ll want 64 Bit. Download this version and double click on the installer once it is finished downloading. 
2. Once the installer (.pkg) has finished downloading (probably to your Downloads folder), double click to start the installation. 
3. Make sure it installs on your primary hard-drive (not an external hard-drive, etc.)
4. To see if your system is configured correctly, find your Terminal application and open it.  You can search for terminal within in Finder if you don’t know where it is. When Terminal opens, type the following (NOTE - do not type the "$", it is symbolizing the *prompt* in the following guide): 

```
$ which conda
```

If you get a response other than “not found” you’re good to go.  If you get a “not found” response, get in touch with a classmate or Emily and she’ll help troublshoot (this isn’t uncommon!). 

#### From here, install JuypterLab

5. Install Jupyter Lab by typing the following into the terminal after the *prompt* (NOTE - do not type the "$", it is symbolizing the *prompt* in the following guide): 

```
$ conda install -c conda-forge jupyterlab
```

6. Follow the prompts to complete the installation. We may do this again after we discuss environments - stay tuned. 
7. Once the installation completes - start Jupyter Lab by typing the following into terminal (do not type the "$"): 

```
$ jupyter lab
```

8. This will open up a Jupyter Lab session in a browser.  Follow the guide here: to start to familiarize yourself with the functions within Jupyter Lab. 
8. Moving on to excercises like the Unix Tutorial - you will want to use the terminal, accessed within Jupyter Lab to access your computers directory structure, etc. 

### Next, move on to [Intro to JupyterLab](../Pages/intro_to_jupyterlab.md) to learn more about the tool. 