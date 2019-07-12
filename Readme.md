# Amazon price checker (APC)

[![Build Status](https://travis-ci.com/olibob/apc.svg?branch=master)](https://travis-ci.com/olibob/apc)

APC is just a little script I decided to play with after seeing a [youtube video from Dev Ed](https://youtu.be/Bg9r_yLk7VY). Nothing serious.

It allows to check the price on amazon articles based on their URL and a threshold price. If the article price drops below the threshold price, your receive and email alerting you that it is time to burn money ;-)
Emails are sent out via gmail SMTP, so you will need a google account.

## Installation

Clone the repo and install the required modules

```
pip install -r requirements.txt
```

## Configuration

Feel free to remove the comments which are there only to define sections. Use the `config-sample.yaml` file and rename it to `config.yaml`.

```
# SMTP user name and password
login: "<your google username (me@gmail.com)>"
password: "<your password or an app password if you use MFA>"
userAgent: "<the user agent to use>"
# Email From,To and Subject
sender: "<from email address>"
receiver: "to email address"
subject: "Price Drop Yo!"
# Articles
articles:
- url: "https://www.amazon.com/.../article1"
  thresholdPrice: 35
- url: "https://www.amazon.com/.../article2"
  thresholdPrice: 155.50
checkingPeriod: 7200
```
For the user agent string, simply open your browser and google "what's my user agent".

## Usage

In the sample configuration, the checking period is set by default to 7200 seconds (2 hours). No need to get crazy about timing, deals usually last an entire day.

Run:

```
python3 app.py
```

You can use Docker or Kubernetes if you do not want to run locally.

## Docker

Build your own image with the included docker file:

```
docker build -t "olibob/apc" .
```

Run the container by injecting your configuration:

```
docker run -d --name apc -v $PWD/config.yaml:/app/config.yaml olibob/apc
```

## Kubernetes

In the Kubernetes directory, create a configmap based on your configuration.

```
kubectl create configmap apc-config --from-file=../config.yaml
```

Modify the apc-deployment.yaml file to deploy your own image or run it with the default image.

Deploy the app.

```
kubectl apply -f deployment.yaml
```

