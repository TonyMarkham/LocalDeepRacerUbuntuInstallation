# **DeepRacer-For-Dummies - Configure aws.cli**

1. Go to [https://aws.amazon.com/](https://aws.amazon.com/).

    1. Click on `My Account`.
    2. Select `AWS Management Console`.
    * ![awscli_01_01_a.png](./img/awscli_01_01_a.png)

2. Use your AWS Credentials:
    1. Enter your `e-mail address` or your `AWS Account`
    2. Click on `Next`.
    * ![awscli_01_02_a.png](./img/awscli_01_02_a.png)

3. Contuinue with your AWS Credentials:
    1. Enter your `password`.
    2. Click on `Next`.
    * ![awscli_01_03_a.png](./img/awscli_01_03_a.png)

4. Locate the `Security, Identity, & Compliance` section:
    1. Click on `IAM`.
    * ![awscli_01_04_a.png](./img/awscli_01_04_a.png)

5. In the `IAM Resources` section:
    1. Click on `Users:`.
    * ![awscli_01_05_a.png](./img/awscli_01_05_a.png)

6. Click on the `Add user` button
    * ![awscli_01_06_a.png](./img/awscli_01_06_a.png)

7. On the 1st `Add user` form:
    1. Enter a `User Name` in the `Set user details` area.
    2. In the `Select AWS Access` area, add a check beside `Programmatic access`.
    3. Click on the `Next: Permissions` button.
    * ![awscli_01_07_a.png](./img/awscli_01_07_a.png)

8. On the 2nd `Add user` form:
    1. Click on the `Attch existing policies directly` button.
    * ![awscli_01_08_a.png](./img/awscli_01_08_a.png)

9. On the 3rd `Add user` form:
    1. Add a check beside `Administrator Access`.
    2. Click on the `Next: Tags` button.
    * ![awscli_01_09_a.png](./img/awscli_01_09_a.png)

10. On the 4rd `Add user` form:
    1. Click on the `Next: Review` button.
    * ![awscli_01_10_a.png](./img/awscli_01_10_a.png)

11. IMPORTANT: Keep the 5th `Add user` page open in order to reference the temporary information:
    1. The `Access Key ID` will be used when you run `aws configure`.
    2. The `Security access key` will be used when you run `aws configure`.
    * ![awscli_01_11_a.png](./img/awscli_01_11_a.png)

12. Configure your aws.cli:

    ```terminal
    aws configure
    ```

    Fill in the promts:

    ```terminal
    AWS Access Key ID [None]: {from Step 11 > 1}
    AWS Secret Access Key [None]: {from Step 11 > 2}
    Default region name [None]: us-east-1
    Default output format [None]: table
    ```

[Back to readme](../README.md)
