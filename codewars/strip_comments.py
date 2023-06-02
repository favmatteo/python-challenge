# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

import re

def strip_comments(strng: str, markers: list):
    rows = strng.split('\n')
    i = 0
    for row in rows:
        news_string = [] # pick it with minor length
        for marker in markers:
            regex: str = '\\'+marker+".*"
            res: re = re.search(regex, row)
            if(res):
                news_string.append(row[:res.start()].rstrip())
        if len(news_string) > 0:
            min = news_string[0]
            for j in range(1, len(news_string)):
                if(len(news_string[j]) < len(min)):
                    min = news_string[j]
            rows[i] = min

        i += 1
    return "\n".join(rows)


print(strip_comments(" a #b\nc\nd $e f g", ['#', '$']))