from pathlib import Path
import os
from InquirerPy import prompt
import json
from shutil import copyfile
from collections import defaultdict
from .constant import SLACK_ASYNC_ALERT_CLI_PATH, CONFIGURE_PATH, CONFIGURE_QUESTIONS


def set_configure():
    """set configure and install slack async alert command if not installed."""
    # prepare directory
    Path(os.path.dirname(CONFIGURE_PATH)).mkdir(exist_ok=True, parents=True)
    if os.path.exists(CONFIGURE_PATH):
        with open(CONFIGURE_PATH) as f:
            prompt_settings = json.load(f)
    else:
        prompt_settings = defaultdict(lambda: None)

    config_qus = []
    for default_qus in CONFIGURE_QUESTIONS:
        default_value = prompt_settings[default_qus["name"]]
        if default_value is not None:
            default_qus["default"] = default_value
        config_qus.append(default_qus)

    answers = prompt(config_qus)
    with open(CONFIGURE_PATH, "w") as f:
        json.dump(answers, f, indent=4, sort_keys=True)

    # check slrt command installed
    return_code = os.system("which slrt")
    # install slrt command, if not exists.
    if return_code != 0:
        # export command
        export_command = f'export PATH="$PATH:{SLACK_ASYNC_ALERT_CLI_PATH}"'
        # find bash type
        shell_type = os.getenv("SHELL").split("/")[-1]
        if shell_type in ["bash", "zsh"]:
            if shell_type == "bash":
                shell_config_path = f"{os.getenv('HOME')}/.bashrc"
            elif shell_type == "zsh":
                shell_config_path = f"{os.getenv('HOME')}/.zshrc"
            with open(shell_config_path, "a") as f:
                f.write(f"\n{export_command}")
        else:
            Warning(
                f'we cannot support your shell program, add "{export_command}" to your shell config file(ex. .bashrc, .zshrc)'
            )
        Path(SLACK_ASYNC_ALERT_CLI_PATH).mkdir(exist_ok=True, parents=True)
        copyfile(
            os.path.join(os.path.dirname(__file__), "slrt"),
            os.path.join(SLACK_ASYNC_ALERT_CLI_PATH, "slrt"),
        )
        os.system(f'chmod 777 {os.path.join(SLACK_ASYNC_ALERT_CLI_PATH, "slrt")}')


def get_configure():
    """get configure of slack async alert"""
    if not os.path.exists(CONFIGURE_PATH):
        raise ValueError(
            f"Slack api key not found, check {CONFIGURE_PATH} file exists, and has api key\n if not exists, use slrt-configure to set api-key."
        )
    with open(CONFIGURE_PATH) as f:
        prompt_settings = json.load(f)

    return prompt_settings
