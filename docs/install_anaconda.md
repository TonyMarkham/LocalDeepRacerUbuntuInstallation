# **DeepRacer-For-Dummies - Install Anaconda and CUDA/CUDNN**

1. Download Anaconda:

    ```terminal
    sudo apt-get update -y && \
        sudo apt-get upgrade -y && \
        cd /tmp && \
        sudo wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
    ```

2. Install Anaconda:

    ```terminal
    bash Anaconda3-2019.03-Linux-x86_64.sh
    ```

3. When promted, agree to the license terms:

    ```
    Welcome to Anaconda3 2019.03

    In order to continue the installation process, please review the license
    agreement.
    Please, press ENTER to continue
    >>>
    …
    Do you approve the license terms? [yes|no]
    ```

4. Complete the Installation:

```
Anaconda3 will now be installed into this location:
/home/$USER/anaconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/$USER/anaconda3] >>>
```

5. Agree to add Anaconda to the `PATH`:

```
Do you wish the installer to prepend the Anaconda3 install location
to PATH in your /home/sammy/.bashrc ? [yes|no]
[no] >>> 
```

6. Go back to your `HOME` directory:

    ```terminal
    cd ~
    ```

7. Activating Anaconda:

    ```terminal
    source ~/.bashrc
    ```

8. Verifying the conda package manager works:

    ```terminal
    conda list
    ```

9. Install CUDA/CUDNN:

    ```terminal
    conda install cudnn==7.3.1 && conda install -c fragcolor cuda10.0
    ```

[Back to readme](../README.md)
