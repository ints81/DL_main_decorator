from DL_main_decorator import DL_main
import argparse

@DL_main(slack_webhook_url="", slack_channel="")
def main(args):
    aaa = args.aaa
    bbb = args.bbb
    ccc = args.ccc
   
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--aaa")
    parser.add_argument("--bbb")
    parser.add_argument("--ccc")
    args = parser.parse_args()
    
    main(args)
