# **DeepRacer-For-Dummies - Install Visual Studio Code**

1. Import the Microsoft GPG key:

    ```terminal
    wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
    ```

2. Enable the Visual Studio Code repository:

    ```terminal
    sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
    ```

3. Update the apt-get repository:

    ```terminal
    sudo apt update
    ```

4. Install the latest version of Visual Studio Code:

    ```terminal
    sudo apt install -y code
    ```

[Back to readme](../README.md)
