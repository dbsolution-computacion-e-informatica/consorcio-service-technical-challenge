Install Python
...


# Install the Serverless Framework
$ npm install serverless -g

# Install the necessary plugins
$ npm install

Install PIP
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
export PATH=$PATH:~/Library/Python/2.7/bin
rm get-pip.py
```

Install boto3
```
pip install boto3
```

Deploy
```
sls deploy
sls fixtures
```