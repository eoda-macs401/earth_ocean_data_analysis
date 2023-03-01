You can copy the below text into a file called: environment.yml, then install this environment by  executing the code:

```
mamba env create -f environment.yml
```

Here's the text to copy to environment.yml file:
____

name: pangeo
channels:
 - conda-forge
dependencies:
 - python=3.9*
 - pangeo-notebook=2021.09.30
 - pip=20
 - adlfs
 - awscli
 - boto3
 - bottleneck
 - cartopy >= 0.20.0
 - cfgrib
 - cmip6_preprocessing
 - ciso
 - dask-ml
 - datashader
 - descartes
 - earthdata
 - eofs
 - erddapy
 - esmpy
 - fastjmd95
 - fsspec
 - fsspec-reference-maker
 - gcsfs
 - gh
 - geocube
 - geopandas
 - geopy
 - geoviews-core
 - gsw
 - h5netcdf
 - h5py
 - holoviews
 - hvplot
 - intake
 - intake-esm
 - intake-geopandas
 - intake-stac
 - intake-xarray
 - ipyleaflet
 - ipytree
 - ipywidgets
 - jupyter-panel-proxy
 - jupyter-resource-usage
 - lz4
 - matplotlib-base
 - metpy
 - nb_conda_kernels
 - nbstripout
 - nc-time-axis
 - netcdf4
 - nomkl
 - numcodecs
 - numpy
 - pandas
 - panel
 - parcels
 - param!=1.11.0
 - prefect
 - pyarrow
 - pycamhd
 - pydap
 - pygeos
 - pystac
 - python-blosc
 - python-gist
 - python-graphviz
 - rasterio
 - rechunker
 - rio-cogeo
 - rioxarray
 - rise
 - s3fs>0.5
 - sat-search
 - sat-stac
 - satpy
 - scikit-image
 - scikit-learn
 - scipy
 - sparse
 - stackstac
 - tiledb-py
 - timezonefinder
 - xarray
 - xarrayutils
 - xarray_leaflet
 - xarray-spatial
 - xcape
 - xcube
 - xesmf
 - xgcm
 - xhistogram
 - xmitgcm
 - xpublish
 - xrft
 - xskillscore
 - zarr