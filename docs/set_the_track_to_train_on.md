# **DeepRacer-For-Dummies - Set the track to train on**

1. Edit the `WORLD_NAME` variable in the `deepracer-for-dummies/docker/.env` file:

* `August Track`

    ```terminal
    sed -i 's/WORLD_NAME=AWS_track/WORLD_NAME=China_track/' ~/git/deepracer-for-dummies/docker/.env
    ```
    
* `September Track`

    * If updating from a fresh clone:

        ```terminal
        sed -i 's/WORLD_NAME=AWS_track/WORLD_NAME=Mexico_track/' ~/git/deepracer-for-dummies/docker/.env
        ```

    * If updating from the August Track:

        ```terminal
        sed -i 's/WORLD_NAME=China_track/WORLD_NAME=Mexico_track/' ~/git/deepracer-for-dummies/docker/.env
        ```

[Back to readme](../README.md)
