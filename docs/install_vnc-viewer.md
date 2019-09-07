# **DeepRacer-For-Dummies - Install VNC Viewer**

1. Change to your `/tmp` folder:

    ```terminal
    cd /tmp
    ```

2. Download VNC Viewer.

    ```terminal
    sudo wget https://www.realvnc.com/download/file/viewer.files/VNC-Viewer-6.19.715-Linux-x64.deb
    ```

3. Install the VNC Viewer

    ```terminal
    sudo dpkg -i VNC-Viewer-6.19.715-Linux-x64.deb
    ```

4. Correct any missing depencies:

    ```terminal
    sudo apt install -f
    ```

5. Start `vncviewer` for the first time:

    ```terminal
    cd ~ && vncviewer
    ```

    Satisfy any windows that pop up and then close the viewer.

[Back to readme](../README.md)
