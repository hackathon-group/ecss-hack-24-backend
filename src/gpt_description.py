from vinted import get_vinted_products
import requests

def gpt_query(img_link):
    api_key = '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'

    payload =  {"model": "gpt-4-vision-preview",
        "messages": [
        {"role": "system",
        "content": [{"type": "text",
                    "text": "You are a british stylist.  Your goal is to describe the clothing item in this image in less than 100 words."}],
        },
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": "What clothing item is in the image?"
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

    headers = {"Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"}
    
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=payload)
    r = response.json()
    print(r)
    print(r["choices"][0]["message"]["content"])

if __name__ == "__main__":
    link_img = get_vinted_products("olive green jumper")[0].image
    gpt_query(link_img)
