import re

def extract_think_tags(input_str):
    # 匹配 <think> 标签内的内容
    think_content = re.findall(r'<think>(.*?)</think>', input_str, re.DOTALL)
    # 将标签内的内容从原字符串中去除
    non_think_content = re.sub(r'<think>.*?</think>', '', input_str, flags=re.DOTALL)
    
    # 将提取的标签内内容拼接成一个字符串（如果有多个 <think> 标签）
    think_content_str = ' '.join(think_content)
    
    return think_content_str, non_think_content

def extract_from_tag(input, tag):
    # 匹配 <think> 标签内的内容
    close_tag = tag[0:1] + '/' + tag[1:]
    output_content = re.findall(rf'{tag}(.*?){close_tag}', input, re.DOTALL)
    
    return output_content


if __name__ == '__main__':
    input_str = "<think>嗯，我现在需要帮用户分析他们所在城市的天气情况，并给出今天的出行建议。首先，用户提供的信息是“查询失败: 暂不支持该城市”，这可能是因为他们的地区没有提供这个城市的天气数据或者有其他限制。我得先确认一下，用户所在的地区是否有对应的天气数据库或服务。假设用户是在北京，因为北京是一个比较大的城市，而且天气数据通常会发布在官方网站上。所以，我应该建议他们去北京的天气网查询最新的天气信息。接下来，我需要分析今天的天气情况，包括温度、风向、湿度等。如果今天是晴朗的，气温适中，风向偏北，湿度较高，那么出行建议应该是轻度运动，避免剧烈运动或直接外出。同时，提醒用户注意保暖，因为虽然天气晴朗，但湿度高可能会让皮肤变热。另外，考虑到北京的气候类型是多云到晴天，风向偏北可能带来北方风，所以需要提醒用户携带雨具，防止被吹淋湿。如果今天还有降雨的可能性，建议提前备好雨具，并在到达后及时转移至阴凉的地方。 最后，我应该给出一个简短的出行建议，包括避免剧烈运动、注意保暖和准备雨具，同时提醒用户保持警惕，确保安全。 </think>根据你的查询信息，我无法直接访问或获取实时天气数据。不过，我可以为你提供一个通用的天气建议： 1. **天气情况分析**：如果你能提供具体的天气信息（如温度、风向、湿度等），我会帮你给出更精准的出行建议。2. **出行建议**：- 如果今天是晴朗的天气，尽量避免剧烈运动或直接外出。- 注意保暖，因为虽然天气晴朗，但湿度较高可能会让皮肤变热。- 预防风向偏北的风险，可以准备雨具并提前转移至阴凉的地方。3. **注意事项**：保持警惕，确保安全，如果遇到可能的危险天气，请及时采取行动。"
    think, non_think = extract_think_tags(input_str)

    print("Think content:", think)
    print("Non-think content:", non_think)
