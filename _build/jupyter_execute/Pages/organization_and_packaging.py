#!/usr/bin/env python
# coding: utf-8

# # Organization and Packaging of Python Projects
# 
# A complex research project often relies and many different programs and software packages to accomplish the research goals. 
# An important part of scientific computing is deciding how to organize and structure the code you use for research.
# A well-structured project can make you a more efficient and effective researcher.
# It is also a key component of [scientific reproducibility](http://lorenabarba.com/blog/barbagroup-reproducibility-syllabus/).
# 
# 
# Just putting all of your code into git repositories won't magically turn a mess of scripts into a beautiful, well-organized project.
# More deliberate effort is required.
# 
# ## Types of Projects
# 
# Not all projects are created equal.
# Based on my experience, I categorize three different types of "research code" scenarios commonly encountered in geosciences.
# 
# 1. **Exploratory analyses**: When exploring a new idea, a single notebook or script is often all we need.
# 1. **A Single Paper**: The "paper" is a standard unit of scientific output. The code related to a single paper usually belongs together. 
# 1. **Reusable software elements**: In the course of our research computing, we often identify specialized routines that we want to package for reuse in other projects, or by other scientists. This is where "scripts" become "software."
# 
# This lecture outlines some suggested practices for each category. 

# ## Exploratory Analysis
# 
# When starting something new, we are often motivated to just start coding and get some results quick.
# This is fine!
# Jupyter notebooks are an ideal format for open-ended exploratory analysis, since they are totally self-contained: they encapsulate text, code, and figures.
# If we find someting cool or useful, it is important to preserve these exploratory notebooks.
# 
# A dedicated github repository can be overkill for a single file.
# Instead, I recommend github's "[gist](https://help.github.com/articles/about-gists/)" mechanism for saving and sharing such "one-off" notebooks and code snippets.
# Gists are like mini repos you can easily share and embed.
# (You can create one right now by going to <https://gist.github.com/>.)
# 
# You can upload any file (including an `.ipynb` notebook file) by dragging and dropping it into the gist website.
# You have the choice of making you gist public or secret. (There is no private option, but a secret gist can only be seen by others if you give them the URL.)
# 
# GitHub's rendering of Gists is a bit buggy. For a more consistent rendering experience, you can share your gist via <http://nbviewer.ipython.org/>.

# ## A Single Paper
# 
# ### Scientific Reproducibility
# 
# Reproducibility is a cornerstone of the scientific process.
# However, today one often reads that science is in the midst of a [reproducibility crisis](http://www.nature.com/news/1-500-scientists-lift-the-lid-on-reproducibility-1.19970).
# This crisis may be due to increasing complexity and cost of scientific analysis, together with mounting pressure to publish as much and as quickly as possible.
# 
# Today almost all earth science relies on some form of computation, from simple statistical analysis and curve fitting to advanced numerical simulation.
# In principle, computational science should be highly reproducible.
# However, it also brings unique challenges.
# A great overview of the challenges and best practices is given in
# _Barba, Lorena A. (2017): Barba-group Reproducibility Syllabus. figshare. <https://doi.org/10.6084/m9.figshare.4879928.v1>._
# Many of the suggestions in this lecture are adopted or paraphrased from _Barba (2017)_.
# 
# Keep in mind that the audience for a reproducibile project is not just other scientists...it's _you_, a year from now, or whenever you need to repeat and / or build on earlier work. Most scientists build on their Ph.D. work for a decade following graduation. Extra time spent on reproducibility now will make you more productive in the long run.
# 
# We begin with an important observation.
# 
# > An article about computational science … is not the scholarship itself, it’s merely scholarship advertisement. The actual scholarship is the complete software development environment and the complete set of instructions which generated the figures.
# 
# _Donoho, D. et al. (2009), Reproducible research in computational harmonic analysis, Comp. Sci. Eng. 11(1):8–18, doi: [10.1109/MCSE.2009.15](http://dx.doi.org/10.1109/MCSE.2009.15)_
# 
# [Sandve et al. (2013)](http://dx.doi.org/10.1371/journal.pcbi.1003285) give some specific recommmendations for computational reproducibility.
# 
# 1. For every result, keep track of how it was produced
# 1. Avoid manual data-manipulation steps
# 1. Archive the exact versions of all external programs used
# 1. Version-control all custom scripts
# 1. Record all intermediate results, when possible in standard formats
# 1. For analyses that include randomness, note underlying random seeds
# 1. Always store raw data behind plots
# 1. Generate hierarchical analysis output, allowing layers of increasing detail to be inspected
# 1. Connect textual statements to underlying results
# 1. Provide public access to scripts, runs, and results
# 
# These recommendations suggest a certain structure for a project.
# 
# ### Project Layout
# 
# A reproducible single-paper project directory structure might look something like this
# 
#     README.md
#     LICENSE
#     environment.yml
#     data/intermediate_results.csv
#     notebooks/process_raw_data.ipynb
#     notebooks/figure1.ipynb
#     notebooks/figure2.ipynb
#     notebooks/helper.py
#     manuscript/manuscript.tex
# 
# A great example of such a paper is [Cesar Rocha](https://crocha700.github.io/)'s Upper Ocean Seasonality project: <https://github.com/crocha700/UpperOceanSeasonality>.
# 
