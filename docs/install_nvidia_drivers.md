# **DeepRacer-For-Dummies - Install nvidia drivers**

**NOTE:** You may need to disable `Secure Boot` in your BIOS.

My motherboard would not allow me to install the nvidia drivers with `Secure Boot` enabled, so I had to disable it in order to proceed.

1. Get a list of available drivers:

    ```terminal
    ubuntu-drivers list
    ```

    The output should liike something like this:

    ```terminal
    nvidia-driver-430
    nvidia-driver-390
    ```

2. Add driver location to the apt-get repositories, then update the repoitories, then install dependancies for the nvidia drivers:

    ```terminal
    sudo add-apt-repository ppa:graphics-drivers && \
    sudo apt-get update && \
    sudo apt install -y nvidia-driver-430 && sudo reboot
    ```

    Continue after the reboot...

3. Verify the driver installation:

    ```terminal
    nvidia-smi
    ```

    You should see output that looks like this:

    ```terminal
    Sat Aug 10 14:43:31 2019
    +-----------------------------------------------------------------------------+
    | NVIDIA-SMI 430.26       Driver Version: 430.26       CUDA Version: 10.2     |
    |-------------------------------+----------------------+----------------------+
    | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
    |===============================+======================+======================|
    |   0  GeForce GTX 108...  Off  | 00000000:01:00.0  On |                  N/A |
    |  0%   47C    P5    21W / 275W |    561MiB / 11175MiB |      0%      Default |
    +-------------------------------+----------------------+----------------------+

    +-----------------------------------------------------------------------------+
    | Processes:                                                       GPU Memory |
    |  GPU       PID   Type   Process name                             Usage      |
    |=============================================================================|
    |    0      1247      G   /usr/lib/xorg/Xorg                           415MiB |
    |    0      1389      G   /usr/bin/gnome-shell                         143MiB |
    +-----------------------------------------------------------------------------+
    ```

4. Install nvidia Cuda Toolkit:

    ```terminal
    sudo apt-get install -y nvidia-cuda-toolkit
    ```

5. Verify:

    ```terminal
    nvcc --version
    ```

    You should see output that looks like this:

    ```terminal
    nvcc: NVIDIA (R) Cuda compiler driver
    Copyright (c) 2005-2017 NVIDIA Corporation
    Built on Fri_Nov__3_21:07:56_CDT_2017
    Cuda compilation tools, release 9.1, V9.1.85
    ```

[Back to README](../README.md)
