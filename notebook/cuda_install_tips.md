# Install CUDA in Ubuntu 

### Introduction 

To install CUDA is painful for most of people since most of data scientists or deep learning researchers are not familiar with system-side knowledge, include me. Few monthes ago, I've successed install CUDA in WINDOWS system, however, for some reasons, the WINDOWS-based version is no longer to satisfited my need. I decided to switch my whole inframe-structure to Ubuntu 14.04 LTS. 

It took me almost 8 hours to sucessfully recover all my base-environment, and the most painful step is to install CUDA. Therefore, I decide to share my sucessful process step-by-step. Hope it will help some people : )


### Step 1 : Pre-installation just follow [officail guild](http://developer.download.nvidia.com/compute/cuda/8.0/secure/prod/docs/sidebar/CUDA_Installation_Guide_Linux.pdf?autho=1478535150_deefbbf1f764ec2a59a02727d0c95c05&file=CUDA_Installation_Guide_Linux.pdf)

- update apt-get
- install GCC G++ 
- sudo apt-get install linux-headers-$(uname -r)
- sudo apt-get install build-essential
- Download your relevant CUDA.run file such as **cuda_8.0.44_linux.run** and chmod 777 it 

### Step 2 : depreciate nouveau since it will cause confiction with Nvidia-driver

Create the /etc/modprobe.d/blacklist-nouveau.conf file with :
 - blacklist nouveau
 - options nouveau modeset=0

Then 
 - $sudo update-initramfs -u
 - Reboot computer to initialize this setting.

### Step 3 : Do the Nvidia-Driver and CUDA installation in TTY1 (Ctrl + Alt + F1).

After reboot, we have to stop any service that is realted to X-server.
- sudo service lightdm stop
- sudo bash cuda-8.0.44_linux.run --no-opengl-libs **(the flag is critial)**
- Accept all setting except the Xserver configuration. **NO for Xserver configurations.**
- (OPTIONAL) sudo modprobe nvidiah

Set Environment path variables in .bashrc and then source it:
- $ export PATH=/usr/local/cuda-8.0/bin:$PATH
- $ export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:$LD_LIBRARY_PATH

### Step 4 : Installation Cudnn

Download Cudnn with right version with your cuda and os-arch
- Download : cudnn-8.0-linux-x64-v5.0-ga.tgz (depend on your version) and unzip it.
- After unzip it, you will find a cuda folder with 2 subfolder lib64 and include

Copy the file from cudnn into the original-CUDA with the corresponding folder
 - cd cuda/lib64 & sudo cp ./* /usr/local/cuda/lib64/ 
 - cd cuda/include & sudo cp cudnn.h /usr/local/cuda/include/
 
Clean and Create right link for cudnn .so, Notice following .so versions are actually depend on your version : 
- cd /usr/local/cuda/lib64/ & sudo rm -rf libcudnn.so libcudnn.so.5 
- sudo ln -s libcudnn.so.5.0.5 libcudnn.so.5 
- sudo ln -s libcudnn.so.5 libcudnn.so 
- OPTIONAL (sudo ln -s /usr/local/cuda/lib64/libcufft.so /usr/lib/libcufft.so) 

### Finally

Once we finished the installation, we could re-opend **lightdm**, or simpliy reboot, and then do the rest of things such as install Torch/Tensorflow/Mxnet/OpenCV/....etc. Good Luck!
