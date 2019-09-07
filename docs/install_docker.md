# **DeepRacer-For-Dummies - Install Docker**

1. Make sure your Ubuntu is clean of Docker components:

    ```terminal
    sudo apt-get remove docker docker-engine docker.io containerd runc
    ```

2. Update your packages:

    ```terminal
    sudo apt-get update
    ```

3. Install some prerequisite packages:

    ```terminal
    sudo apt-get install -y -U \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common
    ```

4. Add the GPG key for the official Docker repository:

    ```terminal
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ```

5. Add the Docker Repository to your apt sources:

    ```terminal
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
    ```

6. Update your packages again:

    ```terminal
    sudo apt-get update
    ```

7. Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:

    ```
    apt-cache policy docker-ce
    ```

8. Install Docker:

    ```terminal
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io
    ```

9. Check that Docker is running:

    ```terminal
    sudo systemctl status docker
    ```

    The output should be similar to the following, showing that the service is active and running:

    ```terminal
    ● docker.service - Docker Application Container Engine
       Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
       Active: active (running) since Sat 2019-08-10 14:48:45 EDT; 47s ago
         Docs: https://docs.docker.com
     Main PID: 8315 (dockerd)
        Tasks: 16
       CGroup: /system.slice/docker.service
               └─8315 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

    Aug 10 14:48:45 ununtu-tony dockerd[8315]: time="2019-08-10T14:48:45.758698003-04:00" level=warning msg="Your kernel does not support cgroup rt runtime"
    Aug 10 14:48:45 ununtu-tony dockerd[8315]: time="2019-08-10T14:48:45.758705200-04:00" level=warning msg="Your kernel does not support cgroup blkio weight"
    Aug 10 14:48:45 ununtu-tony dockerd[8315]: time="2019-08-10T14:48:45.758712580-04:00" level=warning msg="Your kernel does not support cgroup blkio weight_device"
    Aug 10 14:48:45 ununtu-tony dockerd[8315]: time="2019-08-10T14:48:45.758845989-04:00" level=info msg="Loading containers: start."
    Aug 10 14:48:45 ununtu-tony dockerd[8315]: time="2019-08-10T14:48:45.827769825-04:00" level=info msg="Default bridge (docker0) is assigned with an IP address 172.17.0.0/16. Daemon option --bip can be used to set a preferred IP address"
    Aug 10 14:48:45 ununtu-tony dockerd[8315]: time="2019-08-10T14:48:45.861340291-04:00" level=info msg="Loading containers: done."
    Aug 10 14:48:45 ununtu-tony dockerd[8315]: time="2019-08-10T14:48:45.907651660-04:00" level=info msg="Docker daemon" commit=74b1e89 graphdriver(s)=overlay2 version=19.03.1
    Aug 10 14:48:45 ununtu-tony dockerd[8315]: time="2019-08-10T14:48:45.907736004-04:00" level=info msg="Daemon has completed initialization"
    Aug 10 14:48:45 ununtu-tony dockerd[8315]: time="2019-08-10T14:48:45.920939799-04:00" level=info msg="API listen on /var/run/docker.sock"
    Aug 10 14:48:45 ununtu-tony systemd[1]: Started Docker Application Container Engine.
    ```

    Go ahead and \<CTRL-C\> to get out of that command.

10. Check Docker's version:

    ```terminal
    docker --version
    ```

    And you should see something like this:

    ```terminal
    Docker version 19.03.1, build 74b1e89
    ```

[Back to readme](../README.md)
