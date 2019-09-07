# **DeepRacer-For-Dummies - Post Docker Install**

1. Create the docker group.

    ```terminal
    sudo groupadd docker
    ```

2. Add your user to the docker group.

    ```terminal
    sudo usermod -aG docker $USER
    ```

3. Activate the changes to groups:

    ```terminal
    sudo newgrp docker
    ```

4. Verify that you can run docker commands without sudo.

    ```terminal
    docker run hello-world
    ```

5. Configure Docker to start on boot

    ```terminal
    sudo systemctl enable docker
    ```

[Back to readme](../README.md)
