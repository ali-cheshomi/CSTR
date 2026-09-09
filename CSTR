# Copyright 2021 MR_AC. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class cstr(str):
    colorsCode = {
        #text color
        'r':'\033[91m',
        'g':'\033[32m',
        'b':'\033[34m',
        'c':'\033[96m',
        'y':'\033[33m',
        'w':'\033[0m',
        'k': '\033[90m',#gray
        't': '\033[8m', # transparent
        #background text color
        'Rs':'\033[491m',#reset/undo
        'R':'\033[41m',
        'G':'\033[42m',
        'B':'\033[44m',
        'C':'\033[46m',
        'Y':'\033[43m',
        'W':'\033[47m',
        'D':'\033[40m',
        'u': '\033[0m',#reset/undo
        
    }
    
    def __new__(cls, object, encoding="utf-8", errors="strict"):
        raw = cls.__sefrawtext__(
            object,
            colors=list(cls.colorsCode.keys())
        )

        colored = cls.__setcolor__(
            object,
            colors=list(cls.colorsCode.keys()),
            rplace=list(cls.colorsCode.values())
        )

        obj = super().__new__(cls, raw)

        obj._RawText = raw
        obj._ColoredText = colored

        return obj

    def __str__(self):
        return self._ColoredText

    def __setcolor__(txt, colors, rplace):
        for i, cc in enumerate(colors):
            txt = txt.replace(f'^{cc}^', rplace[i])
        return txt + rplace[-1]
    
    def __sefrawtext__(txt, colors):
        for cc in colors:
            txt = txt.replace(f'^{cc}^', '')
        return txt
    
    def __call__(self):
        return self._ColoredText


if __name__ == "__main__":
    text1 = "this is a test1 for color"
    text2 = "this is a test2 for \033[91mcolor\033[0m "
    text3 = cstr("^r^this ^g^is a test3 ^b^for^y^ color")
    
    print(text1)
    print(text2)
    print(text3)
    with open('test.txt','w+') as f:
        f.write(text3)
