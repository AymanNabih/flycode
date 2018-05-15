# FruitFlyCode: A new fruit fly-based algorithm implementation and comparison  with others codes already available

## 1. Setting-up the software stack
Here is how I configured the software platform to run a multi-language environment.

Note: This code has been tested on Ubuntu 16.04 LTS.

**1.1. Installing Docker Community Edition**

- You can check out this procedure to install Docker CE: https://github.com/mchancan/ubuntu-install/blob/master/docker/README.md

**1.2. Installing Jupyter Notebook Data Science Stack**

- Here is how this Docker container works: https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook

- The command I used to install the container:

      sudo docker run -it -p 8888:8888 jupyter/datascience-notebook
- After downloading, the container will be started, just follow the instructions on terminal.



## 2. Configuring fruit fly-based codes available on the literature for comparison purposes

Here I'll show how to configure the environment to run and test at least (5) implementations written in Python and Julia languages

**2.1. Fly-LSH**

Source: [A Python implementation of efficient LSH inspired by fruit fly brain](https://github.com/dataplayer12/Fly-LSH)

- From the Jupyter Notebook obtained in Section 2, open a new Terminal window and from that run:

      cd work/
      git clone https://github.com/dataplayer12/Fly-LSH.git

- Installing `requirements.txt` from the folder Fly-LSH:

      cd Fly-LSH/
      conda install --yes --file requirements.txt
- (Optional) Verifying packages installation:
      
      conda list
- Testing the Fly-LSH notebook: From the Jupyter Notebook, you can open `notebook.ipynb` on the path `work/Fly-LSH/` and then you can try to execute the code and see how it works.

**2.2. BuzzHash**

Source: [A Julia package based on the paper: A neural algorithm for a fundamental computing problem. Science, 358, 6364:793-796](https://github.com/WilCrofter/BuzzHash)

- From the Jupyter Notebook obtained in Section 2, open a new Terminal window and from that run:

      cd work/
      git clone https://github.com/WilCrofter/BuzzHash.git

- Installing the required Julia packages:

      cd BuzzHash/
      
      julia
      
      
      Ṕkg.add("MNIST")
      
      Ṕkg.add("Plots")
      
      Pkg.clone(pwd(), "BuzzHash")
      
      Pkg.build("BuzzHash")
      
      Pkg.test("BuzzHash")
      
      Pkg.add("BuzzHash")

- Testing the Buzz-Hash notebooks: From the Jupyter Notebook, you can open `usage.ipynb and` or `inverse.ipynb` on the path `work/Buzz-Hash/` and then you can try to execute the code and see how it works.

**2.3. FAISS (Facebook AI Research)**

Source: [Facebook AI Research: FAISS library comparison with the "Fly algorithm"](https://github.com/facebookresearch/faiss/wiki/Comparison-with-LSH)

- Note: The code is still in progress, according Facebook AI Research team.

**2.4. A neural algorithm for a fundamental computing problem**

Paper: http://science.sciencemag.org/content/358/6364/793

- Note: We have required the access to the code and will see what happen. Code and data at https://bitbucket.org/navlakha/flylsh is with "access denied." 

**2.5. A clustering neural network model of insect olfaction**

Paper: https://www.biorxiv.org/content/early/2018/01/27/226746

- Note: The code will by posted to GitHub, according to the authors of the paper.



## 3. The proposed Fruit Fly code

- Under development...



## 4. References

[1] Jupyter Notebook Data Science Stack
- https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook

[2] Dasgupta, S., C. F. Stevens, and S. Navlakha (2017). *A neural algorithm for a fundamental computing problem*. Science, 358, 6364:793-796.
- http://science.sciencemag.org/content/358/6364/793

[3] An implementation of efficient LSH, inspired by fruit fly brain algorithm in [2]
- https://github.com/dataplayer12/Fly-LSH
- https://medium.com/@jaiyamsharma/efficient-nearest-neighbors-inspired-by-the-fruit-fly-brain-6ef8fed416ee

[4] A Julia package implementation based on [2]
- https://github.com/WilCrofter/BuzzHash

[5] Facebook AI Research: FAISS library comparison with the "Fly algorithm" in [2]
- https://github.com/facebookresearch/faiss/wiki/Comparison-with-LSH

[6] Pehlevan, C., A. Genkin, D. B. Chklovskii (2018). *A clustering neural network model of insect olfaction*.
- https://www.biorxiv.org/content/early/2018/01/27/226746
