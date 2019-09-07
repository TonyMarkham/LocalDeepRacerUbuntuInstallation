# **DeepRacer-For-Dummies - Install the AWS Commandline Interface (awscli)**

1. Install aws-cli

    ```terminal
    pip install --upgrade --user -y awscli
    ```

2. Update your path to include the default location for aws:

    ```terminal
    echo "export PATH=\"$HOME/.local/bin:$PATH\"" >> ~/.bashrc && source ~/.bashrc
    ```

3. Verify

    ```terminal
    aws --version
    ```

    You should see soething similar to this:

    ```terminal
    aws-cli/1.16.215 Python/3.7.3 Linux/5.0.0-23-generic botocore/1.12.205
    ```

[Back to readme](../README.md)
