# Intro to Unix - For Windows Machines
*Modified from An [Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io)*  

An introduction to basic Unix commands and the file system.  This tutorial is simular to the page - [Introduction to Unix](../Pages/intro_to_unix), but has been modified to (hopefully!) work for folks on a Windows Machine.  For this class you will always simulate a Unix environment on your Windows computer using the Acaconda Prompt or Anaconda Powershell Prompt applications that was installed with Anaconda (accessed via Anaconda3 folder in startup Menu) or **suggested here** via opening up JupyterLab and using the Terminal from there.  There are alternatives to accessing Unix commands on a Windows computer such as by installing Cygwin [(some explanation and links here)](https://sun.iwu.edu/~mliffito/cs_codex/posts/unix-on-your-own-computer/). It usually requires some additional configuration so we'll stick with Anaconda and Jupyter tools here.  Good luck!

*The notes below are modified from the excellent [Unix Shell tutorial ](http://swcarpentry.github.io/shell-novice/) that is freely available on the Software Carpentry website. We highly recommend checking out the full version for further reading. The material is being used here under the terms of the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/).*

***
##### A bit of Background:
Did you know that you can access almost any part of your computer, run most software, and create your own computational tools... all from the command line via a Terminal (Mac, Linux) or simulated via the Anaconda Prompt application on Windows machines? In order to do this (and a generally really really handy skill for most coding efforts), you'll need an understanding of how to navigate a Unix-type operating system.  Macintosh computers are built on a Unix backbone system, so these commands will also work in a Mac Terminal.  If you ever run across a Linux comptuter (running an OS like Ubuntu), it is simular to Unix as well. 

#### Getting Started:
If you are using a winddows computer, most Unix commands will work within the Terminal applicaiton that we can access via Jupyter Lab.  Before we get going, lets use one more package that boosts the Unix functionality.  To do this, install the package called `m2-base`.  
- First open up Anaconda Prompt or Anaconda Powershell Prompt.
Hopefully you see the `(base)` on the left side of your prompt, telling you that Anaconda is running in the background. 
- Next type the following after the prompt (here the prompt is a `$`, don't type that!, everything else though):
`$ conda install m2-base`. When prompted, confirm you want to install  by typing a `y`.
- Once m2-base has completed installation, you can start an instance of Jupyter Lab. **If you are working on a Windows computer, always access terminal by opening up an instance of Anaconda Prompt, and starting Jupyter Lab (type `jupyter lab` at the prompt). Use the Terminal from there.** 

Command output examples are for my computer - yours may be different.  Instead of just typing in commands, pay attention to what you are doing, the output, etc. If something is confusing, get help, or Google it!
***
---

## Navigating Files and Directories in Unix

Several commands are frequently used to create, inspect, rename, and delete files and directories.

To get started, open a terminal using the JupyterLab launcher. You will see
something like this (note, on Windows machines, different for Mac):

~~~
(base) PS C:\Users\emily>
~~~

In general for my tutorials in this book, I use a dollar sign `$` as a **prompt**, which shows us that the shell is waiting for input.  On windows Machines, the Jupyter Lab Terminal applicaiton does not use a dollar sign - it uses a sideways carrot `>`.  When you see this or `$` in the instructions/tutorials, know you do not need to type these!  They symbolize the prompt!

We all have a username that is the log-in user (usually some variation of your name) and the name of the computer you're using (hostname). 

To find out your username in general, you can use the command:

~~~
$ whoami
~~~

When I type the above, I get `desktop-ec5egsb\emily` back, because that's the username on my laptop.  You may see the domain you're logged into ('desktop-ec5egsb' here) and your WWU log-in name if you're on a University computer. 

And to find out your hostname:

~~~
$ hostname
~~~

When I type this, I see: `DESKTOP-EC5EGSB` because that's the name of my laptop computer. 
On the podium computer in IS 410 in IS410 I see `IS410POD01`

### Useful Command: pwd
Next,
let's find out where we are by running a command called `pwd`
(which stands for "print working directory").
At any moment,
our **current working directory**
is our current default directory,
i.e.,
the directory that the computer assumes we want to run commands in
unless we explicitly specify something else.
Here, for me,
the computer's response is `C:\Users\emily`,
which is my **home directory**, or more specifically, the home direcgtory of the user named `emily`.

~~~
$ pwd
~~~


~~~
Path
----
C:\Users\emily
~~~

*Note that one thing that's pretty weird about Windows vs Unix/Linux/MACs is that they show the file structure in simular ways, but Unix,etc. machines use a forward slash `/` and Windows machines use a backslash (like shown above `\`). I don't know why this is but it can get confusing!  Even if you see a tutorial in the future that shows a forward slash - but you're on a PC (Windows) try a backslash if you're referring to directories!*

To understand what a "home directory" is,
let's have a look at how the file system as a whole is organized.  For the
sake of this example, we'll be
illustrating the filesystem on our friend Emily's computer.  After this
illustration, you'll be learning commands to explore your own filesystem,
which will be constructed in a similar way, but not be exactly identical.  

On a Unix (or Mac, based on Unix) computer, the filesystem looks like something this:

![The File System](../images/directory_structure.png)

At the top is the **root directory**
that holds everything else.
We refer to it using a slash character `/` on its own;
this is the leading slash in `/Users/emily`.

Inside that directory are several other directories:
`bin` (which is where some built-in programs are stored),
`lib` (for the software "libraries" used by different programs),
`Users` (where users' personal directories are located, this is true for a Mac. For a pure Unix system, this is called `home`),
`etc` (system-wide configuration files),
and so on. 

**For Windows** computers, the structure is not too different.  The highest directory is usally called by a letter (often C:) with additional drives (like thumb drives) given a different letter. Then there are sub-foders called things like Program Files and Users.  Note the backslashes! `\`:

![The File System](../images/DirectoryStructurePC.png)

### Useful Command: ls

Now let's learn the command that will let us see the contents of our
own filesystem.  We can see what's in our home directory by running `ls`,
which stands for "listing" (note, this is an example, but yours will look different, depending on the folders and files in your home directory):

~~~
$ ls
~~~


~~~
    Directory: C:\Users\emily


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          1/8/2023  10:11 PM                .conda
d-----          1/8/2023  10:10 PM                .continuum
d-----         7/19/2021   7:00 AM                .GMA
d-----         8/10/2020   5:13 PM                .idlerc
d-----         7/17/2021  10:43 AM                .matplotlib
d-r---         4/14/2022  12:07 PM                3D Objects
d-----          2/8/2021  11:25 PM                ComMIT
d-r---         4/14/2022  12:07 PM                Contacts
d-----          8/7/2020  12:08 PM                Documents
d-r---          1/8/2023  10:18 PM                Downloads
d-r---         4/14/2022  12:07 PM                Favorites
d-r---         8/26/2021   7:12 PM                Google Drive
d-r---         8/26/2021   7:12 PM                Videos
-a----         8/26/2021   7:12 PM                myfile.doc
~~~

`ls` prints the names of the files and directories in the current directory in
alphabetical order,
arranged neatly into columns.

### NOTE: The following flag works for UNIX but not WINDOWS via Powershell.  Incluede here for reference:
### Handy "Flag": -F (MAC ONLY)

We can make the `ls` output more comprehensible by using the **flag** `-F`,
which tells `ls` to add a trailing `/` to the names of directories:

~~~
$ ls -F
~~~


~~~
cute_pic_of_Hugo.png  Desktop/ Downloads/ jupyter_notebooks/ Pictures/
~~~

Interestingly - althought the -F command won't work for windows, we don't really need it. If you look in the output of the `ls` command above, all items in our current folder that were directories, showed a `d` listed in the first column.  All files (not folders) did not show this `d`. 

Here,
we can see that our home directory contains mostly **sub-directories**.
Any names in your output that don't have the `d` in front are plain old **files**.

We can also use `ls` to see the contents of a different directory.  Let's take a
look at our `Videos` directory by running `ls Videos`,
i.e.,
the command `ls` with the **argument** `Videos` (the name of the directory we want to look into).
The second argument --- the one *without* a leading dash --- tells `ls` that
we want a listing of something other than our current working directory:

~~~
$ ls Videos
~~~

(Note, try this for one of your own subdirectories, located in *your* hone directory... like maybe `Documents` if it's there. )

~~~
    Directory: C:\Users\emily\Videos


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-r---          2/1/2021  11:50 AM                Captures
~~~

The output is the list of all the files in the `Videos` directory.
Execute the 'ls' command for a directory in your `home` directory such as `Documents` and see what the output is. 


Unless you have a nice neat Documents folder, it's likely you'll see a lot of files and directories listed, but you should recognize some of them as things as documents you've created!

### Useful Command: cd

The command to change locations is `cd` followed by a
directory name to change our working directory.
`cd` stands for "change directory",
which is a bit misleading:
the command doesn't change the directory,
it changes the shell's idea of what directory we are in.

Let's say we want to move to the `Videos` directory.  We can
use the following command to get there:

~~~
$ cd Videos
~~~


This commands will move us from our home directory onto into
the `Videos` folder (or anywhere above or below our home directory). `cd` doesn't print anything,
but if we run `pwd` after it, we can see that we are now
in `\Users\emily\Videos`.

If we run `ls` without arguments now,
it lists the contents of `C:\Users\emily\Videos`,
because that's where we now are.

### Shortcut for Navigation: ..

We now know how to go **down** the directory tree, but
how do we go up?  
There is a shortcut in the shell to move up one directory level
that looks like this:

~~~
$ cd ..
~~~


`..` is a special directory name meaning
"the directory containing this one",
or more succinctly,
the **parent** of the current directory.
Sure enough,
if we run `pwd` after running `cd ..`, we're back in `\Users\emily\` (or whatever yur home directory is):

~~~
$ pwd
~~~

~~~
C:\Users\emily
~~~

### Handy "Flag": -a (MAC ONLY!!)

The special directory `..` doesn't usually show up when we run `ls`.  If we want
to display it, we can give `ls` the `-a` flag:

~~~
$ ls -F -a
~~~


`-a` stands for "show all";
it forces `ls` to show us file and directory names that begin with `.`,
such as `..` (which, if we're in `\Users\emily`, refers to the `\Users` directory)
As you can see,
it also displays another special directory that's just called `.`,
which means "the current working directory".
It may seem redundant to have a name for it,
but we'll see some uses for it soon.

Note that in most command line tools, multiple parameters can be combined
with a single `-` and no spaces between the parameters: `ls -F -a` is
equivalent to `ls -Fa`.

These then, are the basic commands for navigating the filesystem on your computer:
`pwd`, `ls` and `cd`.  

Practice changing directories into a directory within your current working directory by typing the following two commands:

~~~
$ ls 
$ cd <name of a directory>
~~~

Did it work? What is in the new directory you just moved (down) into? (Type `ls` to figure that out.)

### More Practice

Let's explore some variations on those commands.  What happens
if you type `cd` with a `~` symbol after it?

~~~
$ cd ~
~~~


How can you check what happened?  `pwd` gives us the answer!  

~~~   
$ pwd
~~~


~~~
C:\Users\emily
~~~

It turns out that `cd ~` will return you to you to **your home directory**,
which is great if you've gotten lost in your own filesystem.  

### Try this:

As an advance move - let's try navigating *two* directories down in our file structure from our home directory.  I had a directory called `PhotosForBlog` that was on my `Desktop` (you'll have some other folder on your Desktop probably that you could practice with).  There are actually two ways to get to this `PhotosForBlog` directory one with three commands, one with one. The long way first:

~~~
$ cd Documents
$ ls
$ cd PhotosForBlog
~~~

After you did this (maybe with something other than `PhotosForBlog` - a folder in *your* Documents) - did typing `pwd` command give you something like:

~~~
C:\Users\emily\Documents\PhotosForBlog
~~~

If you type `cd ~` it will move you back to your home directory (you knew that). Then we can do the same thing, the slightly easier way. 
This time combine the first and third lines above to one command:

~~~
$ cd \Documents\PhotosForBlog
~~~


Check that we've moved to the right place by running `pwd` again.

If we want to move up one level from the `PhotosForBlog` directory, we could use `cd ..`.  But
there is another way to move to any directory, regardless of your
current location.  

So far, when specifying directory names, or even a directory path (as above),
we have been using **relative paths**.  When you use a relative path with a command
like `ls` or `cd`, it tries to find that location  from where we are,
rather than from the root of the file system.  

However, it is possible to specify the **absolute path** to a directory by
including its entire path from the root directory, which is indicated by a
leading slash.  The leading `\` tells the computer to follow the path from
the root of the file system, so it always refers to exactly one directory,
no matter where we are when we run the command.

This allows us to move to our `Desktop` directory from anywhere on
the filesystem.  To find the absolute path
we're looking for, we can use `pwd` and then extract the piece we need
to move to `Desktop`.  

~~~
$ pwd
~~~


~~~
\Users\emily\Documents\PhotosForBlog
~~~


~~~
$ cd \Users\emily\Videos
~~~


Run `pwd` to ensure that we're in the directory we expect.  


#### Tab Completion

Typing the full path to directories and files can be slow and annoying.
Fortunately, we have "tab completion" to help us. Try typing `cd Des` and then
press the `<tab>`. The system will try to "auto complete" your command.
Pressing tab twice brings up a list of all the files, and so on.
This is called **tab completion**,
and we will see it in many other tools as we go on.

#### Key Points:
- "The file system is responsible for managing information on the disk."
- "Information is stored in files, which are stored in directories (folders)."
- "Directories can also store other directories, which forms a directory tree."
- "`cd path` changes the current working directory."
- "`ls path` prints a listing of a specific file or directory; `ls` on its own lists the current working directory."
- `pwd` prints the user's current working directory.
- `whoami` shows the user's current identity.
- `/` on its own is the root directory of the whole file system.
- A relative path specifies a location starting from the current location.
- An absolute path specifies a location from the root of the file system.
- Directory names in a path are separated with '/' on Unix, but '\\\\' on Windows.
- '..' means 'the directory above the current one'; '.' on its own means 'the current directory'.
- Most files' names are `something.extension`. The extension isn't required, and doesn't guarantee anything, but is normally used to indicate the type of data in the file.
- Most commands take options (flags) which begin with a '-'.

## Working with Files and Directories

We now know how to explore files and directories,
but how do we create them in the first place?
Let's go back to our home directory
and use `ls -F` to see what it contains:

~~~
$ cd
$ pwd
~~~


~~~
\Users\emily\
~~~


~~~
$ ls
~~~


~~~
    Directory: C:\Users\emily


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          1/8/2023  10:11 PM                .conda
d-----          1/8/2023  10:10 PM                .continuum
d-----         7/19/2021   7:00 AM                .GMA
d-----         8/10/2020   5:13 PM                .idlerc
d-----         7/17/2021  10:43 AM                .matplotlib
d-r---         4/14/2022  12:07 PM                3D Objects
d-----          2/8/2021  11:25 PM                ComMIT
d-r---         4/14/2022  12:07 PM                Contacts
d-----          8/7/2020  12:08 PM                Documents
d-r---          1/8/2023  10:18 PM                Downloads
d-r---         4/14/2022  12:07 PM                Favorites
d-r---         8/26/2021   7:12 PM                Google Drive
d-r---         8/26/2021   7:12 PM                Videos
-a----         8/26/2021   7:12 PM                myfile.doc
~~~

Let's create a new directory called `thesis` using the command `mkdir thesis`
(which has no output):

~~~
$ mkdir thesis
~~~


As you might guess from its name,
`mkdir` means "make directory".
Since `thesis` is a relative path
(i.e., doesn't have a leading slash),
the new directory is created in the current working directory:

~~~
$ ls
~~~

~~~
    Directory: C:\Users\emily


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          1/8/2023  10:11 PM                .conda
d-----          1/8/2023  10:10 PM                .continuum
d-----         7/19/2021   7:00 AM                .GMA
d-----         8/10/2020   5:13 PM                .idlerc
d-----         7/17/2021  10:43 AM                .matplotlib
d-r---         4/14/2022  12:07 PM                3D Objects
d-----          2/8/2021  11:25 PM                ComMIT
d-r---         4/14/2022  12:07 PM                Contacts
d-----          8/7/2020  12:08 PM                Documents
d-r---          1/8/2023  10:18 PM                Downloads
d-r---         4/14/2022  12:07 PM                Favorites
d-r---         8/26/2021   7:12 PM                Google Drive
d-r---          1/01/2023  7:00 PM                thesis
d-r---         8/26/2021   7:12 PM                Videos
-a----         8/26/2021   7:12 PM                myfile.doc
~~~


## Good names for files and directories

 Complicated names of files and directories can make your life painful
 when working on the command line. Here we provide a few useful
 tips for the names of your files.

 1. Don't use whitespaces.

    Whitespaces can make a name more meaningful
   but since whitespace is used to break arguments on the command line
   is better to avoid them on name of files and directories.
    You can use `-` or `_` instead of whitespace.

 2. Don't begin the name with `-` (dash).

    Commands treat names starting with `-` as options.

 3. Stick with letters, numbers, `.` (period), `-` (dash) and `_` (underscore).

    Many other characters have special meanings on the command line.
    We will learn about some of these during this lesson.
    There are special characters that can cause your command to not work as
    expected and can even result in data loss.

 If you need to refer to names of files or directories that have whitespace
 or another non-alphanumeric character, you should surround the name in quotes (`""`).


Since we've just created the `thesis` directory, there's nothing in it yet:

~~~
$ ls -thesis
~~~


Let's change our working directory to `thesis` using `cd`.
We then create a blank new file called `draft.txt` using the `touch command`:

~~~
$ cd thesis
$ touch draft.txt
~~~

Now we can edit the file in JupyterLab's text editor.
Let's type in a few lines of text.
Once we're happy with our text, we save the file, and
return to the shell.

`ls` now shows that we have created a file called `draft.txt`:

~~~
$ ls

    Directory: C:\Users\emily\thesis


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          1/8/2023  11:41 PM              0 draft.txt

~~~

Let's tidy up by running `rm draft.txt`:

~~~
$ rm draft.txt
~~~


This command removes files (`rm` is short for "remove").
If we run `ls` again,
its output is empty once more,
which tells us that our file is gone:

~~~
$ ls
~~~


#### Deleting Is Forever

The Unix shell doesn't have a trash bin that we can recover deleted
files from (though most graphical interfaces to Unix do).  Instead,
when we delete files, they are unhooked from the file system so that
their storage space on disk can be recycled. Tools for finding and
recovering deleted files do exist, but there's no guarantee they'll
work in any particular situation, since the computer may recycle the
file's disk space right away.


Let's re-create that file
and then move up one directory to `\Users\emily` using `cd ..`:

~~~
$ touch draft.txt
$ cd ..
~~~

### Warning - following is different on Windows (rm will work without recursive flag!!)
If we try to remove the entire `thesis` directory using `rm thesis`,
we get an error message:

~~~
$ rm thesis
~~~


~~~
rm: cannot remove `thesis`: Is a directory
~~~

This happens because `rm` by default only works on files, not directories.

To really get rid of `thesis` we must also delete the file `draft.txt`.
We can do this with the [recursive](https://en.wikipedia.org/wiki/Recursion) option for `rm`:

~~~
$ rm -r thesis
~~~


#### With Great Power Comes Great Responsibility

 Removing the files in a directory recursively can be very dangerous
 operation. If we're concerned about what we might be deleting we can
 add the "interactive" flag `-i` to `rm` which will ask us for confirmation
 before each step

~~~
 $ rm -r -i thesis
 rm: descend into directory ‘thesis’? y
 rm: remove regular file ‘thesis/draft.txt’? y
 rm: remove directory ‘thesis’? y
~~~


 This removes everything in the directory, then the directory itself, asking
 at each step for you to confirm the deletion.


Let's create that directory and file one more time.

~~~
$ mkdir thesis
$ touch thesis\draft.txt
$ ls thesis
~~~


~~~
draft.txt
~~~


`draft.txt` isn't a particularly informative name,
so let's change the file's name using `mv`,
which is short for "move":

~~~
$ mv thesis\draft.txt thesis\quotes.txt
~~~


The first parameter tells `mv` what we're "moving",
while the second is where it's to go.
In this case,
we're moving `thesis\draft.txt` to `thesis\quotes.txt`,
which has the same effect as renaming the file.
Sure enough,
`ls` shows us that `thesis` now contains one file called `quotes.txt`:

~~~
$ ls thesis
~~~


~~~
quotes.txt
~~~

One has to be careful when specifying the target file name, since `mv` will
silently overwrite any existing file with the same name, which could
lead to data loss. An additional flag, `mv -i` (or `mv --interactive`),
can be used to make `mv` ask you for confirmation before overwriting.

Just for the sake of consistency,
`mv` also works on directories

Let's move `quotes.txt` into the current working directory.
We use `mv` once again,
but this time we'll just use the name of a directory as the second parameter
to tell `mv` that we want to keep the filename,
but put the file somewhere new.
(This is why the command is called "move".)
In this case,
the directory name we use is the special directory name `.` that we mentioned earlier.

~~~
$ mv thesis\quotes.txt .
~~~


The effect is to move the file from the directory it was in to the current working directory.
`ls` now shows us that `thesis` is empty:

~~~
$ ls thesis
~~~


Further,
`ls` with a filename or directory name as a parameter only lists that file or directory.
We can use this to see that `quotes.txt` is still in our current directory:

~~~
$ ls quotes.txt
~~~


~~~
quotes.txt
~~~


The `cp` command works very much like `mv`,
except it copies a file instead of moving it.
We can check that it did the right thing using `ls`
with two paths as parameters --- like most Unix commands,
`ls` can be given multiple paths at once:

~~~
$ cp quotes.txt thesis\quotations.txt
$ ls quotes.txt thesis\quotations.txt
~~~


~~~
quotes.txt   thesis\quotations.txt
~~~


To prove that we made a copy,
let's delete the `quotes.txt` file in the current directory
and then run that same `ls` again.

~~~
$ rm quotes.txt
$ ls quotes.txt thesis\quotations.txt
~~~


~~~
ls: cannot access quotes.txt: No such file or directory
thesis\quotations.txt
~~~

This time it tells us that it can't find `quotes.txt` in the current directory,
but it does find the copy in `thesis` that we didn't delete.

### Key Points
- `cp old new` copies a file.
- `mkdir path` creates a new directory.
- `mv old new` moves (renames) a file or directory.
- `rm path` removes (deletes) a file.
- Use of the Control key may be described in many ways, including `Ctrl-X`, `Control-X`, and `^X`.
- The shell does not have a trash bin: once something is deleted, it's really gone.
- Depending on the type of work you do, you may need a more powerful text editor than Nano.

## Learning More

The goal of this lesson was to familiarize you with the basics of working
with files and directories.
There is a **lot more** to the unix shell and filexsystem than what we have  covered here!
To ge deeper with self study, we recommend the excellent
[Software Carpentry Unix Shell Lesson](https://swcarpentry.github.io/shell-novice/),
on which the above material was based.
