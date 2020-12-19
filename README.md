# DL Main Decorator

```python
# Usage
# Program name : main.py

from DL_main_decorator import DL_main
import argparse

@DL_main(slack_webhook_url="<slack app webhook URL>", slack_channel="chan to receive a msg")
def main(args):
    aaa = args.aaa
    bbb = args.bbb
    ccc = args.ccc
   
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--aaa")
    parser.add_argument("--bbb")
    parser.add_arugment("--ccc")
    args = parser.parse_args()
    
    main(args)

"""
python main.py --aaa=xxx --bbb=yyy --ccc=zzz

The Result:
=============== ARGS INFO ===============

aaa : xxx
bbb : yyy
ccc : zzz

=============== ARGS INFO ===============

And send a message(Host name, Start time, End time, Duration) to the slack channel
"""
```



DL Main Decorator는 두 가지 개인적인 불편함이 있어 만들었다.

1. 딥러닝이 끝나면 슬랙으로 메세지 받으면 좋겠다.

2. 딥러닝 프로세스를 실행할 때 내가 적은 configuration이 출력되면 좋겠다.

   1. 내가 제대로 configuration을 넣었는지를 확인할 수 있고,

   2. 실험 결과를 리다이렉션을 통해 파일로 만들었을 때, 해당 파일이 어떤 configuration으로 돌았는지 확인이 가능하다.