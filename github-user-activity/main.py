import argparse
import asyncio
import parser

import fetcher

argparser = argparse.ArgumentParser()
argparser.add_argument("username", type=str)
args = argparser.parse_args()

user_data = asyncio.run(fetcher.get_user_data_async(args.username))

messages = parser.parse(user_data)

for message in messages:
    print(f"° {message}")
