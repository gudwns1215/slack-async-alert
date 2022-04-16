from typing import List, Optional

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from .configure import get_configure
from .constant import CONFIGURE_PATH


class SlackClient:
    def __init__(
        self,
        stack_thread: bool = False,
        noty_interval_steps: Optional[List[int]] = None,
    ):
        config = get_configure()
        slack_key = config.get("slack_key", None)
        user_id = config.get("user_id", None)
        hardware_identifier = config.get("hardware_identifier", None)
        assert slack_key is not None, f"cannot find slack_key! check {CONFIGURE_PATH}!"
        assert user_id is not None, f"cannot find user_id! check {CONFIGURE_PATH}!"
        self.stack_thread = stack_thread
        self.thread_ts = None
        self.client = WebClient(token=slack_key)
        self.noty_interval_steps = noty_interval_steps
        self.user_id = user_id
        self.hardware_identifier = hardware_identifier

    def __call__(
        self,
        message: str,
        file_paths: Optional[List[str]] = None,
        each_upload: bool = False,
        reply_broadcast: bool = False,
    ):
        try:
            if file_paths is not None:
                if len(file_paths) > 1:
                    response = self.multi_upload_file(
                        message, file_paths, reply_broadcast, each_upload=each_upload
                    )
                else:
                    response = self.single_upload_file(
                        message, file_paths, reply_broadcast
                    )
            else:
                response = self.send_message(message, reply_broadcast)

            if self.stack_thread and self.thread_ts is None:
                self.thread_ts = response["ts"]
        except SlackApiError as e:
            print(e)

    def single_upload_file(self, message, file_paths, reply_broadcast):
        return self.client.files_upload(
            channels=self.user_id,
            initial_comment=message,
            file=file_paths[0],
            filename=file_paths[0],
            thread_ts=self.thread_ts,
            reply_broadcast=reply_broadcast,
        )

    def multi_upload_file(
        self, message, file_paths, reply_broadcast, each_upload: bool = False
    ):
        if each_upload:
            for file_path in file_paths:
                response = self.single_upload_file(
                    message, [file_path], reply_broadcast
                )
                message, reply_broadcast = "", False  # only send one message
            return response

        for file in file_paths:
            upload = self.client.files_upload(file=file, filename=file)
            message = message + "<" + upload["file"]["permalink"] + "| >"
        return self.client.chat_postMessage(
            channel=self.user_id,
            text=message,
            thread_ts=self.thread_ts,
            reply_broadcast=reply_broadcast,
        )

    def send_message(self, message, reply_broadcast):
        response = self.client.chat_postMessage(
            channel=self.user_id,
            text=message,
            thread_ts=self.thread_ts,
            reply_broadcast=reply_broadcast,
        )
        return response
