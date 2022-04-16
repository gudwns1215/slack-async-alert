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
slrt echo "hello world"
```


## installation

1. pip install slack_async_alert

2. run slrt-configure command.
    - it will ask slack-api-key, user_id, server identifier
    - slack-api-key: bot api key, that can made from slack custom app.
    - user_id: slack user id
    - server identifier: identifier that you can recognise where your program is finished.

3. finished, if slrt command not works, restart shell.


## Uninstallation

1. pip uninstall slack_async_alert

2. rm -r ~/.slack_async_alert/

3. delete 'export PATH="$PATH:$HOME/.slack_async_alert/bin"' term from your shell config file.


## How to build package.
```
python setup.py bdist_wheel && pip install -e .
twine upload dist/{generated dist file path}
```
