#!/usr/bin/python3
import sys
import httpx
import asyncio
import json

EXECUTE = 'https://emkc.org/api/v2/piston/execute'
RUNTIMES = 'https://emkc.org/api/v2/piston/runtimes'

# python example: https://pastebin.com/raw/cmJ5Kaqw
# javascript example: todo


async def runtimes():
    async with httpx.AsyncClient() as client:
        response = await client.get(RUNTIMES)
    return json.dumps(response.json(), indent=2)


async def execute(lang, code, *args):
    async with httpx.AsyncClient() as client:
        execute = await client.get(code)

        body = {
            "language": lang,
                "version": "*",
                "files": [
                    {
                    #"name": "main.py",
                    "content": execute.text
                    }
                ],
                "stdin": "",
                "args": ["1", "2", "3"],
                "compile_timeout": 10000,
                "run_timeout": 3000,
                "compile_memory_limit": -1,
                "run_memory_limit": -1
        }

        response = await client.post(EXECUTE, json=body)
    return json.dumps(response.json(), indent=2)


print(asyncio.run(execute(sys.argv[1], sys.argv[2])))
#print(asyncio.run(execute('py', TEST_CODE)))
#print(asyncio.run(runtimes()))
