import pyautogui
import time
import platform
import asyncio
import random

screen_size = (1920, 1080)


def altTab():
	key = 'alt'
	if platform.system() == "Darwin":
		key = "command"
	pyautogui.keyDown(key)
	time.sleep(.2)
	pyautogui.press('tab')
	time.sleep(.2)
	pyautogui.keyUp(key)

async def moveMouse():
	rand_x = random.randint(0, screen_size[1])
	rand_y = random.randint(0, screen_size[0])
	print(f'move mouse to {rand_x} {rand_y}')
	pyautogui.moveTo(rand_x, rand_y, duration=0.5)
	await asyncio.sleep(1)


async def writeBeeMovie(loop):
	with open('beemovie.txt', 'r+') as beemovie:
		lines = beemovie.readlines()
		for line in lines:
			asyncio.ensure_future(moveMouse())
			print(line)
			pyautogui.write(line)
			await asyncio.sleep(1)

altTab()
loop = asyncio.get_event_loop()
loop.run_until_complete(writeBeeMovie(loop))
print('End')

