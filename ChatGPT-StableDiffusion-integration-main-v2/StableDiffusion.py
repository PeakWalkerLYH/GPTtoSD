import os
import nlpcloud
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

client = nlpcloud.Client(
    "stable-diffusion", os.getenv('STABLEDIFFUSION_TOKEN'), True, lang="zho_Hans")


def generate_image(prompt):
    try:
        print("第三阶段进行，生成图像提示词中......")
        response = client.image_generation(prompt)
        print("第三阶段完成")
        return response['url']
    except Exception as e:
        print(e)
        print("第三阶段出错！")
        return None

# Van Gogh and Mona Lisa drinking coffee together under the Eiffel Tower.
# a cat sitting on top of a building, Josephine
# 梵高和蒙娜丽萨坐在埃菲尔铁塔下喝着咖啡。
"""
风格：
fantasy style, 
editorial fashion magazine photoshoot, 

细节：
highly detailed.
incredibly highly detailed and realistic

艺术家风格：
 Josephine Wall（梦幻）， John Singer Sargent
"""