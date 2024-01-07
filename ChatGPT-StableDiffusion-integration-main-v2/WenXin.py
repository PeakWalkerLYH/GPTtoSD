import requests
import json
import time

API_KEY = "GD3uiAVFyHgmwK55RCLo0OZH"
SECRET_KEY = "zMrk4TtjEnf74LdqlYfwHeax3rlGVacp"


def post_message(prompt):
    try:
        """
        百度大模型 某些提示词报错
        """
        print("第三阶段进行，根据图像提示词生成图像......")
        # post
        url = "https://aip.baidubce.com/rpc/2.0/ernievilg/v1/txt2img?access_token=" + get_access_token()
        """
        style
        目前支持风格有：
        探索无限、古风、二次元、写实风格、浮世绘、low poly 、未来主义、
        像素风格、概念艺术、赛博朋克、洛丽塔风格、巴洛克风格、超现实主义、
        水彩画、蒸汽波艺术、油画、卡通画
        """
        payload = json.dumps({
            "text": prompt,
            "resolution": "1024*1024",
            "style": "写实风格"
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response1 = requests.request("POST", url, headers=headers, data=payload)
        # 使用 json() 方法获取 JSON 对象
        json_obj = response1.json()
        # 从 JSON 对象中取出 taskId 后的数字
        print(response1.text)
        task_id_number = json_obj['data']['taskId']

        # print(type(response1))  <class 'requests.models.Response'>
        print("第三阶段完成，已生成图片！")
        return task_id_number

    except Exception as e:
        print(e)
        print("第三阶段出错！")
        return None


# request
def get_picture(image_prompt):
    t_id = post_message(image_prompt)
    url = "https://aip.baidubce.com/rpc/2.0/ernievilg/v1/getImg?access_token=" + get_access_token()

    payload = json.dumps({"taskId": t_id})
    time.sleep(10)
    # print(payload)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response2 = requests.request("POST", url, headers=headers, data=payload)
    # 使用 json() 方法获取 JSON 对象
    json_obj = response2.json()
    # 从 JSON 对象中取出 taskId 后的数字
    image_url = json_obj['data']['imgUrls'][0]['image']

    # 返回图片url
    return image_url


# 获取access_token
def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


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