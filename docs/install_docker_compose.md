# **DeepRacer-For-Dummies - Install Docker Compose**

1. Run this command to download the current stable release of Docker Compose:

    ```terminal
    sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ```

2. Apply executable permissions to the binary:

    ```terminal
    sudo chmod +x /usr/local/bin/docker-compose
    ```

3. Test Docker-Compose:

    ```terminal
    docker-compose --version
    ```

    And you should see something like this:

    ```terminal
    docker-compose version 1.24.1, build 4667896b
    ```

[Back to readme](../README.md)
