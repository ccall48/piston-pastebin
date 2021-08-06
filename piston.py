import sys
import httpx
import asyncio
import json

RUNTIMES = 'https://emkc.org/api/v2/piston/runtimes'
EXECUTE = 'https://emkc.org/api/v2/piston/execute'


async def runtimes():
    """
    Return a json list all current languages and versions available for those languages
    on the public piston instance (Also saves list to you machine).
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(RUNTIMES)
        with open('languages.json', 'w') as file:
            file.write(response.text)
    return json.dumps(response.json(), indent=4)


async def execute(lang, code_url, args):
    async with httpx.AsyncClient() as client:
        execute = await client.get(code_url)

        body = {
            "language": lang,
                "version": "*",
                "files": [
                    {
                    "content": execute.text
                    }
                ],
                "compile_timeout": 10000,
                "run_timeout": 3000,
                "compile_memory_limit": -1,
                "run_memory_limit": -1
        }

        if type(args) is str:
            body['stdin'] = args

        if type(args) is list:
            body['args'] = args

        response = await client.post(EXECUTE, json=body)
    return json.dumps(response.json(), indent=4)


def runner():
    if sys.argv[1] == 'runtimes':
        return asyncio.run(runtimes())

    if len(sys.argv) == 3:
        print('NO INPUTS')
        return asyncio.run(
            execute(sys.argv[1], sys.argv[2], args='')
        )

    if len(sys.argv) > 4:
        if sys.argv[3] == '-argv':
            print('ARGV:', sys.argv[4:])
            return asyncio.run(
                execute(sys.argv[1], sys.argv[2], sys.argv[4:])
            )

        if sys.argv[3] == '-stdin':
            print('STDIN:', ' '.join(sys.argv[4:]))
            return asyncio.run(
                execute(sys.argv[1], sys.argv[2], '\n'.join(sys.argv[4:]))
            )

print(runner())
