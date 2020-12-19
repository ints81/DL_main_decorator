import datetime
import json
import socket
import requests
import sys


def DL_main(slack_webhook_url=None, slack_channel=None):
    if slack_webhook_url is None:
        print("ERROR: Specify slack webhook_url")
        sys.exit(1)
    elif slack_channel is None:
        print("ERROR: Specify slack channel")
        sys.exit(1)

    def decorator(func):

        def wrapper(cmd_args=None):
            if cmd_args is not None:
                print("=============== ARGS INFO ===============\n")
                cmd_args_dict = vars(cmd_args)
                for n, v in cmd_args_dict.items():
                    print("{} : {}".format(n, v))
                print("\n=============== ARGS INFO ===============\n")

            host_name = socket.gethostname()
            start_time = datetime.datetime.now()

            func(cmd_args)

            end_time = datetime.datetime.now()
            duration = end_time - start_time

            contents = ["Your training job is complete",
                        "Machine name : {}".format(host_name),
                        "Start time : {}".format(start_time.strftime("%Y-%m-%d %H:%M:%S")),
                        "End time : {}".format(end_time.strftime("%Y-%m-%d %H:%M:%S")),
                        "Duration : {}".format(str(duration))]

            # Send a message to slack
            message = {
                "username": "Deep Learning Notifier",
                "channel": slack_channel,
                "text": '\n'.join(contents),
            }
            requests.post(slack_webhook_url, json.dumps(message))
        return wrapper

    return decorator

