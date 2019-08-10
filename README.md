# **Deep Racer**

## **Install Ubuntu**

## **Install nvidia drivers**

* NOTE: You may need to disable `safety boot`

1. Type the following and examine the ouput to ensure that you have an nvidia gpu:

    ```terminal
    hwinfo --gfxcard --short
    ```

    You should see output that looks like this:

    ```terminal

    ```

2. Use the Ubuntu Software & Updates GUI to install the `nvidia-driver-430 (proprietary, tetsed)`

3. Roboot.

    ```terminal
    sudo reboot
    ```

4. Verify

    ```terminal
    nvidia-smi
    ```

## **Install Docker**

1. Update your packages

    ```terminal
    sudo apt-get update
    ```

2. Install packages to allow for https delivery of packages

    ```terminal
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    ```

3. Add the GPG key for the official Docker repository

    ```terminal
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ```

4. Add the Docker Repository to your apt sources

    ```terminal
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
    ```

5. Update your packages again

    ```terminal
    sudo apt-get update
    ```

6. Make sure you are about to install from the Docker repo instead of the default Ubuntu repo by listing the current candidates:

    ```terminal
    sudo apt-cache policy docker-ce
    ```

    1. You'll see output like this, although the version number for Docker may be different:

        ```terminal
        docker-ce:
        Installed: (none)
        Candidate: 18.03.1~ce~3-0~ubuntu
        Version table:
            18.03.1~ce~3-0~ubuntu 500
                500 https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
        ```

        Notice that docker-ce is not installed, but the candidate for installation is from the Docker repository for Ubuntu 18.04 (bionic).

7. Finally, install Docker:

    ```terminal
    sudo apt-get install docker-ce
    ```

    Docker should now be installed, the daemon started, and the process enabled to start on boot. Check that it's running:

8. Check that its working:

    ```terminal
    sudo systemctl status docker
    ```

    The output should be similar to the following, showing that the service is active and running:

    ```terminal
    docker.service - Docker Application Container Engine
    Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
    Active: active (running) since Thu 2018-07-05 15:08:39 UTC; 2min 55s ago
        Docs: https://docs.docker.com
    Main PID: 10096 (dockerd)
    Tasks: 16
    CGroup: /system.slice/docker.service
            ├─10096 /usr/bin/dockerd -H fd://
            └─10113 docker-containerd --config /var/run/docker/containerd/containerd.toml
    ```

    Installing Docker now gives you not just the Docker service (daemon) but also the docker command line utility, or the Docker client. We'll explore how to use the docker command later in this tutorial.

## **Install git**

```terminal
sudo apt-get install git-core
```

## **Create a Directory for cloning git Repositories**

```terminal
mkdir git && cd git
```

## **Clone the Repository**

```terminal
git clone https://github.com/ARCC-RACE/deepracer-for-dummies.git &&cd deepracer-for-dummies &&./init.sh
```
