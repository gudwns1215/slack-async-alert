# slack async alert
this program sends alarm when passed command finished, and tell you that program successfully finished or not.

this program can be used, when running program that takes long time work.


## usage
```
slrt {some command}
```


## example
```
slrt python run.py --some random_args --that can_be_passed
```


## installation

1. pip install slack_async_alert

2. run slrt-configure command.

3. finished, if slrt command not works, restart shell.


## how to build package.
python setup.py bdist_wheel && pip install -e .

