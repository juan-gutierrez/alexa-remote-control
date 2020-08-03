#!/usr/bin/env python3

import aiohttp
import asyncio
import pysmartthings

token = 'bc6c2c46-bfe6-43fb-9420-e901ada0f20b'

async def print_devices():
    async with aiohttp.ClientSession() as session:
        print("Open session")
        api = pysmartthings.SmartThings(session, token)
        print("Opened session")
        devices = await api.devices()
        locations = await api.locations()
        print(len(locations))
        for device in devices:
            print("{}: {}".format(device.device_id, device.label))
            await device.status.refresh()
            print(device.status.values)
            print("")
            print("")
            print(device.status.switch)
            print("")
            print("")
            print(device.status.level)
            print("")
            print("")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_devices())
    loop.close()

if __name__ == '__main__':
    main()
