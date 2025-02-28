# -*- coding: utf-8 -*-
import os

import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import GroupMessage,MessageAudit
from plugins import weather_api,stock_price,hot_trend
from plugins.utils import extract_think_tags
from langchain_community.llms import Ollama
test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()


class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")
    async def on_message_audit_pass(self, message: MessageAudit):
        print(f"消息审核通过：{message.message_id}")

    async def on_message_audit_reject(self, message: MessageAudit):
        print(f"消息审核未通过：{message.message_id}")

    async def on_group_at_message_create(self, message: GroupMessage):
        llm=Ollama(model="deepseek-r1:1.5b",temperature=1.3)
        msg = message.content.strip()
        member_openid = message.author.member_openid
        print("[Info] bot 收到消息：" + message.content)

        if msg == f"我喜欢你":
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=f"我也喜欢你")
        elif msg.startswith("/天气"):
            city_name = msg.replace("/天气", "").strip()
            result = weather_api.format_weather(city_name)
            advice = llm.invoke("这是我所在的城市的天气情况：\n" + result + "\n 请根据我所在的地区的天气情况，结合地区的背景给出今日的出行建议")
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=f"{result}")
            think, non_think = extract_think_tags(advice)
            await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                content=f"{non_think}")
        elif msg.startswith("/股价"):
            stock_name = msg.replace("/股价", "").strip()
            res = stock_price.get_stock_price(stock_name)
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                content=f"{res}")
        elif msg.startswith("/热搜"):
            res = hot_trend.get_data()
            print(res)
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                content=f"{res}")
        else:
            res = llm.invoke(msg)
            think, non_think = extract_think_tags(res)
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=f"{non_think}")

        _log.info(messageResult)


if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_messages=True,message_audit=True)
    client = MyClient(intents=intents, is_sandbox=True)
    client.run(appid=test_config["appid"], secret=test_config["secret"])
