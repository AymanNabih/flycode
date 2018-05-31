FruitFlyCode: A new fruit fly's brain-based algorithm implementation and comparison with other codes already available
================================================================================================================

1. [Hardware](#1-hardware)
2. [Setting the software stack](#2-setting-the-software-stack)
   1. [Using Docker Community Edition](#21-using-docker-community-edition)
   2. [Using Anaconda](#22-using-anaconda)
3. [Configuring fruit fly-based codes available on the literature](#3-configuring-fruit-fly-based-codes-available-on-the-literature)
   1. [Fly-LSH](#31-fly-lsh)
   2. [BuzzHash](#32-buzzhash)
   3. [FAISS by Facebook AI Research](#33-faiss-by-facebook-ai-research)
   4. [A neural algorithm for a fundamental computing problem](#34-a-neural-algorithm-for-a-fundamental-computing-problem)
   5. [A clustering neural network model of insect olfaction](#35-a-clustering-neural-network-model-of-insect-olfaction)
4. [The proposed Fruit Fly code](#4-the-proposed-fruit-fly-code)
5. [References](#5-references)

   
# 1. Hardware
The code shown here has been tested on Ubuntu 16.04 LTS, the hardware configuration is detailed as follow:
- 1x Processor Intel Core i7-8700K @ 3.7GHz (6 CPU cores, 12 threads)
- 4x Memory 8 GB DIMM DDR4 2400 MHz (32 GB RAM)
- 2x GeForce GTX 1080 Ti, 11 Gbps, 11 GB GDDR5X, 3584 CUDA cores, 352-bit, 484 GB/sec (7168 CUDA cores)
- 1x SSD 512 GB for OS
- 1x HDD 4 TB for storage


# 2. Setting the software stack
Here is how I configured the software platform to run a multi-language environment, including Python 2/3, Julia, Octave, TensorFlow and others, from a Jupyter Notebook.

I have configured and tested the software I need using two (2) environments: a) Docker containers, b) Anaconda.

## 2.1 Using Docker Community Edition

First, let's see how to configure a Docker container.

### Installing Docker CE

- You can check out this procedure to install Docker CE: https://github.com/mchancan/ubuntu-install/blob/master/docker/README.md

### Installing Jupyter Notebook Data Science Stack

- Here is how this Docker container works: https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook

- After Docker installation, the command I used to download the image and run the container is:

      sudo docker run -it --network host -p 8888:8888 jupyter/datascience-notebook
- The container will be started, just follow the instructions on terminal.

## 2.2 Using Anaconda

Now, let's se how to use Anaconda distribution to build our environment.

### Install Anaconda

-  Follow the instructions here: https://github.com/mchancan/ubuntu-install/blob/master/anaconda.md

### Install Julia Language

- Follow instructions here: https://github.com/mchancan/ubuntu-install/blob/master/julia.md

Other references about Julia Language and Anaconda:

- https://haroldsoh.com/2016/04/28/set-up-anaconda-ipython-tensorflow-julia-on-a-google-compute-engine-vm/
- http://people.duke.edu/~ccc14/cspy/Local_Installation.html


# 3. Configuring fruit fly-based codes available on the literature

Here I'll show how to configure the environment to run and test at least (5) implementations written in Python, Julia and other languages for comparison purposes.

## 3.1 Fly-LSH

Source: [A Python implementation of efficient LSH inspired by fruit fly brain](https://github.com/dataplayer12/Fly-LSH)

- From the Jupyter Notebook obtained in Section 2, open a new Terminal window and from that run:

      cd work/
      git clone https://github.com/dataplayer12/Fly-LSH.git

- (If you are using Docker containers) Installing `requirements.txt` from the folder Fly-LSH:

      cd Fly-LSH/
      conda install --yes --file requirements.txt
      
- (If you are on Anaconda) Install ´tensorflow´ from a new Terminal window:

   Source: https://anaconda.org/conda-forge/tensorflow

      conda install -c conda-forge tensorflow 
      
      # Verifying packages installation
      conda list

- Testing the Fly-LSH notebook: From the Jupyter Notebook, you can open `notebook.ipynb` on the path `work/Fly-LSH/` and then you can try to execute the code and see how it works.

## 3.2 BuzzHash

Source: [A Julia package based on the paper: A neural algorithm for a fundamental computing problem. Science, 358, 6364:793-796](https://github.com/WilCrofter/BuzzHash)

- From the Jupyter Notebook obtained in Section 2, open a new Terminal window and from that run:

      cd work/
      git clone https://github.com/WilCrofter/BuzzHash.git

- Installing the required Julia packages:

      cd BuzzHash/
      
      julia
      
      
      Pkg.add("MNIST")
      
      Pkg.add("Plots")
      
      Pkg.clone(pwd(), "BuzzHash")
      
      Pkg.build("BuzzHash")
      
      Pkg.test("BuzzHash")
      
      Pkg.add("BuzzHash")

- Testing the Buzz-Hash notebooks: From the Jupyter Notebook, you can open `usage.ipynb and` or `inverse.ipynb` on the path `work/Buzz-Hash/` and then you can try to execute the code and see how it works.

## 3.3 FAISS by Facebook AI Research

Source: [Facebook AI Research: FAISS library comparison with the "Fly algorithm"](https://github.com/facebookresearch/faiss/wiki/Comparison-with-LSH)

- Note: The code is still in progress, according Facebook AI Research team.

## 3.4 A neural algorithm for a fundamental computing problem

Paper: http://science.sciencemag.org/content/358/6364/793

- Note: We have required the access to the code and will see what happen. Code and data at https://bitbucket.org/navlakha/flylsh is with "access denied." 

## 3.5 A clustering neural network model of insect olfaction

Paper: https://www.biorxiv.org/content/early/2018/01/27/226746

- Update (May 24, 2018): Code is now available here: https://github.com/alexgenkin/Neural_Clustering
- Note (May 10, 2018): The code will by posted to GitHub, according to the authors of the paper.


# 4. The proposed Fruit Fly code

- Under development...



# 5. References

[1] Jupyter Notebook Data Science Stack
- https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook

[2] Dasgupta, S., C. F. Stevens, and S. Navlakha (2017). **A neural algorithm for a fundamental computing problem**. Science, 358, 6364:793-796.
- http://science.sciencemag.org/content/358/6364/793

[3] An implementation of efficient LSH, inspired by fruit fly brain algorithm in [2]
- https://github.com/dataplayer12/Fly-LSH
- https://medium.com/@jaiyamsharma/efficient-nearest-neighbors-inspired-by-the-fruit-fly-brain-6ef8fed416ee

[4] A Julia package implementation based on [2]
- https://github.com/WilCrofter/BuzzHash

[5] Facebook AI Research: FAISS library comparison with the "Fly algorithm" in [2]
- https://github.com/facebookresearch/faiss/wiki/Comparison-with-LSH

[6] Pehlevan, C., A. Genkin, D. B. Chklovskii (2018). **A clustering neural network model of insect olfaction**.
- https://www.biorxiv.org/content/early/2018/01/27/226746

## About me

Visit my Google Scholar, GitHub, LinkedIn and other profiles:

- [Google Scholar Profile](https://scholar.google.com/citations?hl=es&user=iK7xhJ4AAAAJ)
- [GitHub Repository](https://github.com/mchancan)
- [LinkedIn Profile](https://www.linkedin.com/in/mchancan/)
- [Twitter Profile](https://twitter.com/mchancan)
- [My webpage](https://sites.google.com/view/mchancan/research)
