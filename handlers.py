import os
import aiohttp
import asyncio
from dotenv import load_dotenv

load_dotenv()


HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY', ''),
}
print(HEADERS)

async def gpt_handler(message: str) -> str:
    json_data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
            'role': 'user',
            'content': message,
            },
            {
            "role": "assistant",
            "content": "\nYou are helpfull assistant to answer users questions."
            }
        ],
        'temperature': 0.7,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            'https://api.openai.com/v1/chat/completions',
            headers=HEADERS,
            json=json_data
        ) as response:

            print("Status:", response.status)
            answer = await response.json()
            return answer['choices'][0]['message']['content']


if __name__ == '__main__':
    print(asyncio.run(gpt_handler("Tell a joke.")))
