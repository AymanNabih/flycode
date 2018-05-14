# FlyCode: A new fruit fly-based algorithm implementation and comparison  with others codes already available


## Preparing the environment
Here is how I configured the software platform to run a multi-language environment

Note: This code has been tested on Ubuntu 16.04 LTS.

**1. Installing Docker Community Edition**

- You can check out this procedure to install Docker CE: https://github.com/mchancan/ubuntu-install/blob/master/docker/README.md

**2. Installing Jupyter Notebook Data Science Stack**

- Here is how this Docker container works: https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook

- The command I used to install the container:

      sudo docker run -it -p 8888:8888 jupyter/datascience-notebook
- After downloading, the container will be started, just follow the instructions on terminal.

**3. Configuring and Testing the Fly-LSH code**

Source: [A Python implementation of efficient LSH inspired by fruit fly brain](https://github.com/dataplayer12/Fly-LSH)

- From the Jupyter Notebook obtained in Section 2, open a new Terminal window and from that run:

      cd work/
      git clone https://github.com/dataplayer12/Fly-LSH.git

- Installing requirements.txt in folder Fly-LSH:

      cd Fly-LSH/
      conda install --yes --file requirements.txt
- (Optional) Verify packege installations:
      
      conda list
- Testing the Fly-LSH notebook: From the Jupyter Notebook, you can open `notebook.ipynb` on the path `work/Fly-LSH/` and then you can try to execute the code and see how it works.

**4. Configuring and Testing the BuzzHash**

Source: [A Julia package based on the paper: A neural algorithm for a fundamental computing problem. Science, 358, 6364:793-796](https://github.com/WilCrofter/BuzzHash)

- From the Jupyter Notebook obtained in Section 2, open a new Terminal window and from that run:

      cd work/
      git clone https://github.com/WilCrofter/BuzzHash.git

- Installing the required Julia Packages:

      cd BuzzHash/
      julia
      
      Ṕkg.add("MNIST")
      
      Ṕkg.add("Plots")
      
      Pkg.clone(pwd(), "BuzzHash")
      
      Pkg.build("BuzzHash")
      
      Pkg.test("BuzzHash")
      
      Pkg.add("BuzzHash")

- Testing the Buzz-Hash notebooks: From the Jupyter Notebook, you can open `usage.ipynb and` or `inverse.ipynb` on the path `work/Buzz-Hash/` and then you can try to execute the code and see how it works.

## References

[1] Jupyter Notebook Data Science Stack
- https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook

[2] An implementation of efficient LSH inspired by fruit fly brain
- https://github.com/dataplayer12/Fly-LSH
- https://medium.com/@jaiyamsharma/efficient-nearest-neighbors-inspired-by-the-fruit-fly-brain-6ef8fed416ee

[3] A Julia package based on S. Dasgupta, C. F. Stevens, and S. Navlakha (2017). A neural algorithm for a fundamental computing problem. Science, 358, 6364:793-796
- https://github.com/WilCrofter/BuzzHash
