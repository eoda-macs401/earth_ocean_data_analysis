# Final Projects

Note - this page contains ideas for a ambitious final project - like that which would be appropriate for a typical 4-credit course.  For the Spring 2022 (2 credit) version of this course, the final projects will be paired down to something closer to a single assignment-scale effort.  Some of the informaiton outlined below may still be useful for brainstorming your project, consdiering data sources, computational tools and submission formats.  

Although the learning goals, dataset requrements, and analysis requirements for our paired down final projects are simular to those outlined below, consider how these can be scaled to a ~2 week effort for 2022:

### Learning Goals

The goal of the final project is to assess your ability to combine and apply the skills you have learned in class in the context of a real-world research problem. Our class has mostly focused on tools for data analysis and visualization, so this must be the focus of your final project. Specifically, we seek to assess your ability to do the following tasks:

*   Discover and download real datasets in standard formats (e.g. CSV, netCDF)
*   Load the data into Pandas or Xarray, performing any necessary data cleanup (dealing with missing values, proper time encoding, etc.) along the way.
*   Perform realistic scientific calculation involving, for example tasks such as grouping, aggregating, and applying mathematical formulas.
*   Visualize your results in well-formatted plots.

### Dataset Requirements

Your datasets can involve data collected by yourself or your lab, or can come from a public data repository. Ideally, your choice of dataset should be driven by your research. It is acceptable (and encouraged) to have your final project for this class involve an ongoing research project. _However, it is not acceptable to have your final project overlap with the final project for another class._

If you don't know what dataset to use, here are a couple of links to get you started:

*   [IRI Data Library](http://iridl.ldeo.columbia.edu/)
*   [USGS Data Catalog](https://data.usgs.gov/datacatalog/)
*   [NOAA National Climate Data Center](https://www.ncdc.noaa.gov/)
*   [NASA Earth Science Data](https://earthdata.nasa.gov/)

You may use just one dataset, or you may choose to combine multiple datasets, depending on your scientific question.

### Analysis Requirements

The goal here is the same as with any science project: to use the data to investigate a scientific question or hypothesis. In order to succeed on the project, you will have to draw on your experience _outside_ our class, from your science-focused classes or independent research, in order to define a scientifically interesting question. It is also acceptable to use this project to reproduce the results from a published study that you find interesting, provided you have access to the original data.

Whatever you choose, you should _clearly define a hypothesis or scientific question that you aim to investigate with your analysis_. This will determine what you have to do.

The results of this analysis will be figures. Beautiful figures which clearly provide answers to your question / hypothesis. Your notebook should contain at least 4 and no more than 8 figures. If you have closer to 4, they should be complex, multi-panel figures. All figures must have titles, clearly labeled axes, informative colormaps / colorbars, and legends, where appropriate.

### Technical Requirements

Your final project must meet the following technical requirements

*   A _single jupyter notebook_
*   Stored in a standalone public github repo
*   All data is either stored in the repo itself or downloaded / accessed from within the notebook (no manual download steps)
*   Complete explanatory text / equations included in the notebook as markdown cells
*   Notebook must execute in sequence with no errors


You _must_ use either Pandas or Xarray (or both) in some part of your project. You _may_ use other scientific python libraries as well, if you wish, to facilitate some analysis that is not possible with Xarray / Pandas alone. Some libraries you may wish to consider are:

```{admonition} Note for 2022
:class: tip

We will not get to Pandas and Xarray until the very end of the quarter. As such, the requirement listed above will be relaxed.  We'll try to explore these tools around the time you are ramping up your Final Project plan, and I encourage you to use them to import and organize data - but any method you find to access data for analysis will be acceptable. 
```

*   [SciPy](https://docs.scipy.org/doc/scipy/reference/) for interpolation, signal processing, spectral analysis, linear algebra, and other general purpose scientific computing routines
*   [Statsmodels](https://github.com/statsmodels/statsmodels) for advanced statistical analysis
*   [Scikit-image](https://scikit-image.org/) for image processing
*   [Scikit-learn](https://scikit-learn.org/stable/) for machine learning
*   [XESMF](https://xesmf.readthedocs.io/en/latest/) for regridding of gridded data
*   [Pyresample](https://pyresample.readthedocs.io/en/latest/) for resampling (reprojection) of satellite data
*   [metpy](https://unidata.github.io/MetPy/latest/index.html) a collection of tools in Python for reading, visualizing, and performing calculations with weather data

### Project Approval

You must have your dataset(s) and general scope for your project improved by the instructor. The approval process works like this:

*   Create a new public github repo for your project
*   Add a `README.md` file which contains the scientific question / hypothesis you plan to investigate, links to the relevant datasets, and a three sentence summary of the analysis you plan to do.
*   Submit a link to your project repo using the method indicated by the instructor. 

### In-Class Presentations (*time permitting for 2022*)

You are asked to give a 5-minute presentation about your project. Do not prepare any slides. Instead, make your presentation by opening your notebook from GitHub on the presentation computer and walking us through parts of it. Your presentation should be concise and cover the following topics:

*   What data did you analyze and how did you load it?
*   What is the most interesting figure you made? (Show us the figure.)
*   What was the biggest challenge you faced in completing your project.

_Don't forget to make your project repo **public**; otherwise we won't be able to see it._
