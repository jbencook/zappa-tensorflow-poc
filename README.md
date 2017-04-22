# TensorFlow on AWS Lambda with Zappa

This is a proof of concept with TensorFlow working on AWS Lambda.

To try this out change the s3 bucket in [settings](./zappa_settings.json) to one that you own. Then run something like the following:

```
virtualenv tf-test
source tf-test/bin/activate
pip install -r requirements.txt
pip uninstall lambda-packages
pip install git+https://github.com/jbencook/lambda-packages.git
zappa deploy dev
```
