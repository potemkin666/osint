import requests
from PIL import Image
from io import BytesIO

# Function to display an image from a URL
def show_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

# Example usage
image_url = "https://cdn.gencraft.com/prod/user/5b48ab66-497c-42e6-bdae-e9f21f22c9b4/fe2d185b-634c-4f93-aa5a-f7d9c875c558/image/image0_0.jpg?Expires=1735816098&Signature=RkXjVLJ6Q6-Odt7xT2USzpa7sw~bxE9Kwhk4c-5fCRGEfnDD-cJwhxJGHlNbdXEmLAAoe0GBzbgxqYW~Yf5g5gsyGVvPrK9Ye-sY~3QpoPgqibt-xCptJ0bcPRQR4YYEI5sNj0Yt3MS65ioXLgjKprZCf7yYm~b6lIGkGyrG8mjH5ediw4pvAGprhdJtpCyffgijEJ0jRY0WG1s55bF9HmxPnznZiMgki7kIgjKZdKiQz9Rl2WYRAU1~Kr3SK71sW7bdiET3bxCsbZ8jb6ez-2~tfCl~~dVgezReOPd0fBmrwmNpEtVb1UHwJgwUvpnNKgJtc8R-9iVKTufiuC6jzg__&Key-Pair-Id=K3RDDB1TZ8BHT8"
show_image_from_url(image_url)