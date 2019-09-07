# **DeepRacer-For-Dummies - Install nvidia-docker**

1. Set the `distribution` variable:

    ```terminal
    distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
    ```

2. Set the gpgkey:

    ```terminal
    sudo curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
    ```

3. Add nvidia-docker to your apt-get's distribution list:

    ```terminal
    curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
    ```

4. Update the apt-get repositories:

    ```terminal
    sudo apt-get update
    ```

5. Install the `nvidia-docker2`

    ```terminal
    sudo apt-get install -y nvidia-docker2
    ```

6. Restart Docker:

    ```terminal
    sudo systemctl restart docker
    ```

[Back to readme](../README.md)
