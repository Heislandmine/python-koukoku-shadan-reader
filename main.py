from telnetlib import Telnet
from typing import List

with Telnet("koukoku.shadan.open.ad.jp", 23) as tn:
    line: List[str] = []
    while True:
        try:
            body = tn.read_eager().decode("shift_jis")
            if (body != "\n"):
                line.append(body)
            else:
                print("".join(line))
                line.clear()

        except EOFError as e:
            break
        except UnicodeDecodeError as e:
            continue