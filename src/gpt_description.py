from src.vinted import get_vinted_products
import requests
import os

API_KEY = os.getenv('OPENAI_API_KEY')

def gpt_query(item_name, img_link):

    description_item = "Describe the " + str(item_name)

    payload =  {"model": "gpt-4-vision-preview",
        "messages": [
        {"role": "system",
        "content": [{"type": "text",
                    "text": "Your goal is to solely describe the item specified in this image in less than 100 words. Don't mention anything else, no background, no other items in the image, just the item mentioned in the prompt."}],
        },
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": description_item
            },
            {
                "type": "image_url",
                "image_url": {
                "url": img_link
                }
            }
            ]
        }
        ],
        "max_tokens": 500
    }

    headers = {"Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"}
    
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=payload)
    r = response.json()
    print(r)
    result = r["choices"][0]["message"]["content"]
    print(result)
    return result


if __name__ == "__main__":
    item = get_vinted_products("red hat")[0]
    item_name = item.name
    link_img = item.image
    gpt_query(item_name, link_img)
