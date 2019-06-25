# Convolutional VAE
A step by step guide for creating your very own variational autoencoder.

## Python Environment
For this tutorial, we'll create a new Python environment so you can run the scripts. You'll need a package-handler, such as [Anaconda](https://docs.conda.io/en/latest/miniconda.html), or [MiniConda](https://docs.conda.io/en/latest/miniconda.html). The packages required is listed in requirements.txt, but I'll guide you thorugh the installation process if you're using Anaconda or MiniConda. First, make sure you are in the directory of this tutorial. Than, we'll create an environment:
```
conda create --name VAE_guide python==3.6
```
Let's activate it:
```
conda activate VAE_guide
```
And than, we install the required packages
```
pip install -r requirements.txt
```

## Jupyter notebooks
[Jupyter notebook](http://www.jupyter.org) is a web application for running and sharing code and documentation in a user friendly and readable format. To start, run jupyter from the terminal (note: You should be in the folder where "VAE guide.ipynb" is located, which should be the root folder of this repo):

```
(ml) $ jupyter notebook
```

If you open [http://localhost:8888](http://localhost:8888) you should see the file-structure of the folder where you run the command, and if any .ipynb-files (such as the guide) exists. Simply click "VAE guide.ipynb" to get started.

A readable WEB-version of the gude can be found [here](https://nbviewer.jupyter.org/github/epimedai/VAE/blob/master/VAE%20guide.ipynb).
