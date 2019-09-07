# **DeepRacer-For-Dummies - Mount a Drive as `~/git`**

1. Create a `git` sub-directory in your `HOME` directory:

    ```terminal
    sudo mkdir $HOME/git && \
    sudo chown $USER:$USER $HOME/git
    ```

2. Install `gparted`.

    ```terminal
    sudo apt-get install -y gparted
    ```

3. Start `gparted`.

    ```terminal
    sudo gparted
    ```

4. In the top-Right corner of the `gparted` window, select the hard drive that you want to mount.
5. `Right-Click` on the partition that you want to mount and select `information`.
6. Copy the `UUID` of the partition that you want to mount.
7. Add this partition as your `~/git` sub-directory:

    ```terminal
    UUID=f3e3c791-9bec-410c-bcc6-7e88a2efd226 && \
    echo "UUID=\"${UUID}\"  ${HOME}/git  ext4  defaults  0  0" | sudo tee -a /etc/fstab && \
    sudo mount -a
    ```

8. Confirm that it allocated properly:

    ```terminal
    sudo df -h $HOME/git
    ```

    You should see output that looks like this:

    ```terminal
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/sdb1       1.8T   77M  1.7T   1% /home/tony/git
    ```

[Back to readme](../README.md)
