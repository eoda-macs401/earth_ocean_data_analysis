# Assignment 2: Files, Git, and Github

## Create a Dummy Resume Repository

Use JupyterLab to launch a terminal and use the terminal to do the following tasks:

1. Create a new directory called `resume` on your new "eoda" thumbdrive

To get to your new thumbdrive from the command line (terminal), you'll need to change directories into it.  You should know how to do this from the Unix Tutorial, however, you may not knwo how to find it on your system.

#### For Mac users 
External hard drives tend to 'auto mount' to the `/Volumes` directory. So to move to within your new thumb drive, you could type the following into terminal: 

```
$ cd /Volumes/eoda
$ mkdir resume
```
Then change directories into your new `resume` directory (you know how to do that!)
#### For Windows users 
External hard drives tend to 'auto mount' to a new directory - kind of like your main C:\\ directory, but with a diffrent letter (i.e. `E`, `W`... something else). You may need to find it in the filesystem within Windows to know where to go, but then to get there in JupyterLab Terminal, the command will likely look something like this (for `E` directory example mount point): 

```
$ cd E:\\eoda
$ mkdir resume
```
Then change directories into your new `resume` directory (you know how to do that!)
Get help from Emily if you're having trouble with this. 


2. Create an empty file within this directory called `Readme.md`

#### Now use JupyterLab to edit the file:

1. Navigate to the directory in the file browser

```{warning}
This is one thing that can be a bit tricky when we're using an external harddrive. When you open JupyterLab from your home directory - this is the top "parent" directory we can access easily. My recommendation for accessing your new file in that case:
- re-start JupyterLab from your eoda directory (cd to `/Volumes/eoda` in Terminal before opening JupyterLab - on a Mac, to your jump drive location on a PC. Then you'll have easy access to any materials on that drive.)
```


1. Open `Readme.md` in the text editor
1. Open `Readme.md` in in Markdown Preview
1. Arrange these files side-by-side so you can see your document rendered
1. Edit the file in the editor. Add the following information:

    1. Top level heading with your name
    1. An image. It can be a photo of you or, if you prefer, a photo of your spirit animal.
    1. Secondary heading entitled "Education"
    1. A list of schools you attended, hyperlinked to the websites of those insitutions
  
1. Save the file

  
    #### Tip on incorporating an image.  
    To add an image, you'll want to save your picture, maybe in a jpg or png format, in your new repository directory.  Then to show it in your markdown file, you can use the following syntax:
    
    ```
    ![alt text for screen readers](/relative/path/to/image.png "Text to show on mouseover")
    ```
    
    Also note - if your photo is a weird size, try Googling solutions!
    
#### Now go back to the terminal and do the following:

1. Initialize a new git repository in the `resume` directory
1. Add the `Readme.md` file and your photo to the repository. 
1. Create a new commit with a commit message (see [Intro to Git](../Pages/intro_to_git) if you've forgotten how to do this)
1. Check the git log to see your commit history
1. Go to GitHub and create a [new public repository](https://github.com/new) entitled `resume`
1. Push your local resume repository to GitHub following the instructions (this is the "... or push an existing repository from the command line" option). There will be three commands to execute - GitHub tells you what to do but... **Before doing anything, double check the 'ssh' is selected to use your SSH Key for authentification**
1. View your online resume at `http://github.com/<your github username>/resume`

Finally, go back to the editor and add a new subsection called "Research Interests" to your `Readme.md` file. Update your local git repository and push your changes to GitHub. Verify that the remote repository is updated.

To "hand in" this part of the assignment, put a link to it in the `Readme.md` file in the next part.


## Create your Assignments Repository

Now that you know how to create a git repository, you should create your assignments repository.

- Create a new directory called `eoda-assignments` in your home directory.
- Create a `Readme.md` markdown file that contains your name and a link to your "resume" repo.
- Also place your "First_Class_Reflection.md" file from last week in the new assignments director (in your new repo). 
- Initialize a new git repository 
- Add the file and make your first commit
- Create a new **private** repository on GitHub called `eoda-assignments`. (Call it exactly like that. Do not vary the spelling, capitalization, or punctuation.)
- Push your `eoda-assignments` repository to GitHub
- On GitHub, go to "settings" -> "collaborators" and add `rolandocean`.
- Push new commits to this repository whenever you are ready to hand in your assignments.
