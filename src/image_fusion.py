import replicate
import time
import os

os.environ['REPLICATE_API_TOKEN'] = 'r8_WqZPAPwLUKebW0RyJs9i8B0Ph4RdAUX40DeG5'


def image_fusion_replicate(portrait_url: str, product_url: str) -> str:
    output = replicate.run(
    "omniedgeio/virtual-dressing:d6835398c2147f0a09a99a9f6cb59f7f87c9f72c67078f3858fc51e7eefde338",
    input={
        "seed": 0,
        "steps": 30,
        "model_image": portrait_url,
        "garment_image": product_url,
        "guidance_scale": 3
        }
    )

    return output


if __name__ == "__main__":
    image_fusion(
        'https://ecss-hack-24-backend.onrender.com/images/2d74f900-f500-4fdf-b412-57a5b243fca3/portrait.jpg',
        'https://images1.vinted.net/t/03_00af4_AwCktTj9sGd2dkrqbEnpMWGz/f800/1710627962.jpeg?s=639f08db24be1b29f28e3a3b5724dd4adb9f2044'
    )