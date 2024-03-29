from pydantic import BaseModel
from vinted_scraper import VintedScraper

class VintedProduct(BaseModel):
    name: str
    price: str
    size: str
    image: str
    url: str

def get_vinted_products(query) -> list[VintedProduct]:
    scraper = VintedScraper("https://www.vinted.co.uk")  # Init the scraper with the baseurl
    params = {
        "search_text": query
        # Add other query parameters like the pagination and so on
    }
    items = scraper.search(params)  # Get all the items
    itemInfoList = []
    for item in items: # Get item details
        itemName = item.title
        itemPrice = str(item.total_item_price) + " " + item.currency
        itemSize = item.size_title
        itemImage = item.photo.full_size_url
        itemURL = item.url
        itemInfoList.append(VintedProduct(name=itemName, price=itemPrice, size=itemSize, image=itemImage, url=itemURL))
    return itemInfoList
    print(itemInfoList)
   # scraper.item(item.id) # get more info about a particular item


if __name__ == "__main__":
    get_vinted_products("olive green jumper")


# RESPONSE EXAMPLE
'''
VintedItem(
    id=4223919090,
    title="Operation - Buzz Lightyear",
    price=2.0,
    is_visible=1,
    discount=None,
    currency="USD",
    brand=VintedBrand(
        id=None,
        title="Hasbro",
        slug=None,
        favourite_count=None,
        pretty_favourite_count=None,
        item_count=None,
        pretty_item_count=None,
        is_visible_in_listings=None,
        requires_authenticity_check=None,
        is_luxury=None,
        path=None,
        url=None,
        is_favourite=None,
    ),
    is_for_swap=False,
    url="https://www.vinted.com/items/4223919090-operation-buzz-lightyear",
    promoted=False,
    photos=[
        VintedImage(
            id=17231823138,
            width=678,
            height=800,
            temp_uuid=None,
            url="https://images1.vinted.net/t/02_00c58_Gcu9C92W2532qfRdgf8h4UMp/f800/1710445799.jpeg?s=236d660040dfd8c42cfa722ae9f4d7c69656843d",
            dominant_color="#827B84",
            dominant_color_opaque="#DAD7DA",
            thumbnails=[
                VintedMedia(
                    type="thumb70x100",
                    url="https://images1.vinted.net/t/02_00c58_Gcu9C92W2532qfRdgf8h4UMp/70x100/1710445799.jpeg?s=064cc7922091bccd14350988dec9f1d3ccef4d3d",
                    width=70,
                    height=100,
                    original_size=None,
                ),
                VintedMedia(
                    type="thumb150x210",
                    url="https://images1.vinted.net/t/02_00c58_Gcu9C92W2532qfRdgf8h4UMp/150x210/1710445799.jpeg?s=9abbe9e390c69b3098f05f8740e810c7bbffe85f",
                    width=150,
                    height=210,
                    original_size=None,
                ),
                VintedMedia(
                    type="thumb310x430",
                    url="https://images1.vinted.net/t/02_00c58_Gcu9C92W2532qfRdgf8h4UMp/310x430/1710445799.jpeg?s=c4d254f2b6af0f5f4b8c2d60a21377783051075a",
                    width=310,
                    height=430,
                    original_size=None,
                ),
                VintedMedia(
                    type="thumb428x624",
                    url="https://images1.vinted.net/t/02_00c58_Gcu9C92W2532qfRdgf8h4UMp/f800/1710445799.jpeg?s=236d660040dfd8c42cfa722ae9f4d7c69656843d",
                    width=362,
                    height=428,
                    original_size=True,
                ),
                VintedMedia(
                    type="thumb624x428",
                    url="https://images1.vinted.net/t/02_00c58_Gcu9C92W2532qfRdgf8h4UMp/f800/1710445799.jpeg?s=236d660040dfd8c42cfa722ae9f4d7c69656843d",
                    width=529,
                    height=624,
                    original_size=True,
                ),
                VintedMedia(
                    type="thumb364x428",
                    url="https://images1.vinted.net/t/02_00c58_Gcu9C92W2532qfRdgf8h4UMp/f800/1710445799.jpeg?s=236d660040dfd8c42cfa722ae9f4d7c69656843d",
                    width=308,
                    height=364,
                    original_size=True,
                ),
            ],
            is_suspicious=False,
            orientation=None,
            high_resolution=VintedHighResolution(
                id="02_00c58_Gcu9C92W2532qfRdgf8h4UMp",
                timestamp=1710445799,
                orientation=None,
            ),
            full_size_url="https://images1.vinted.net/tc/02_00c58_Gcu9C92W2532qfRdgf8h4UMp/1710445799.jpeg?s=de05e891919dc6bbcfa34aea918990bc8d5ef4c4",
            is_hidden=False,
            image_no=1,
            is_main=True,
        )
    ],
    favourite_count=9,
    is_favourite=False,
    badge=None,
    conversion=None,
    service_fee=0.8,
    total_item_price=2.8,
    view_count=0,
    size_title="",
    content_source="search",
    accepted_pay_in_methods=None,
    user_id=None,
    description=None,
    brand_id=None,
    size_id=None,
    status_id=None,
    disposal_conditions=None,
    owner_id=None,
    country_id=None,
    catalog_id=None,
    color1_id=None,
    color2_id=None,
    package_size_id=None,
    is_hidden=None,
    is_reserved=None,
    reserved_for_user_id=None,
    is_unisex=None,
    is_closed=None,
    active_bid_count=None,
    moderation_status=None,
    last_push_up_at=None,
    package_size_standard=None,
    item_closing_action=None,
    related_catalog_ids=None,
    related_catalogs_enabled=None,
    size=None,
    composition=None,
    extra_conditions=None,
    is_for_sell=None,
    is_for_give_away=None,
    is_handicraft=None,
    is_processing=None,
    is_draft=None,
    label=None,
    real_value_numeric=None,
    original_price_numeric=None,
    created_at_ts=None,
    updated_at_ts=None,
    user_updated_at_ts=None,
    push_up_interval=None,
    can_be_sold=None,
    can_feedback=None,
    item_reservation_id=None,
    receiver_id=None,
    promoted_until=None,
    vas_gallery_promoted_until=None,
    vas_gallery_promoted_created_at=None,
    discount_price_numeric=None,
    author=None,
    book_title=None,
    isbn=None,
    measurement_width=None,
    measurement_length=None,
    measurement_unit=None,
    transaction_permitted=None,
    video_game_rating_id=None,
    item_attributes=None,
    is_story_uploaded=None,
    discount_price=None,
    can_edit=None,
    can_delete=None,
    can_reserve=None,
    can_mark_as_sold=None,
    can_transfer=None,
    instant_buy=None,
    can_close=None,
    can_buy=None,
    can_bundle=None,
    can_ask_seller=None,
    can_favourite=None,
    user_login=None,
    city_id=None,
    city=None,
    country=None,
    is_mobile=None,
    bump_badge_visible=None,
    path=None,
    created_at=None,
    color1=None,
    color2=None,
    description_attributes=None,
    video_game_rating=None,
    status="Very good",
    performance=None,
    stats_visible=None,
    can_push_up=None,
    can_vas_gallery_promote=None,
    vas_gallery_promoted=None,
    size_guide_faq_entry_id=None,
    localization=None,
    is_upload_story_button_visible=None,
    offline_verification=None,
    offline_verification_fee=None,
)
'''