main_page = dict(
    main_page_logo = "//a[@id='nav-logo-sprites']"
)

side_navbar_menu = dict(
    menu_all_id = "nav-hamburger-menu",
    see_all_css = ".hmenu-item.hmenu-compressed-btn",

    electronics = "//div[contains(text(),'Electronics')]",
    computer_accessory = "//a[contains(text(),'Computers & Accessories')]",
    computer_tablets = "//span[contains(text(),'Computers & Tablets')]",
)

computer_tablet_page = dict(
    product_list_classname = 's-result-item',

    product_index = '//div[contains(@data-index, "{}")]',
    product_link = "//div[contains(@data-index, '{}')]/descendant::a",
    product_price = "//span[@id='price_inside_buybox']",
    product_title = "//span[@id='productTitle']",
    availability = "//div[@id='availability']",
    product_quantity = "//select[@id='quantity']",
    add_to_card_id = "add-to-cart-button",
)

cart_checkout = dict(
    to_cart_checkout_id = "nav-cart-count-container",
    cart_item_list_css=".sc-list-body.sc-java-remote-feature>div",

    proceed_to_checkout = "//div[contains(text(),'Proceed to checkout')]",
    cart_item_title = "//div[@data-asin='{}']/descendant::span[contains("
                      "@class, 'product-title')]"
)



