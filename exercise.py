optin: bool


class WebPush:
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        print("Push gönderildi!{}".format(self.push_type))


class TriggerPush(WebPush):
    trigger_page = str

    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 trigger_page):
        self.trigger_page = trigger_page
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)


class BulkPush(WebPush):
    send_date = int

    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 send_date):
        self.send_date = send_date
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)


class SegmentPush(WebPush):
    segment_name = str

    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 segment_name):
        self.segment_name = segment_name
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)


class PriceAlertPush(WebPush):
    price_info = int
    Discount_rate = float

    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 price_info, Discount_rate):
        self.price_info = price_info
        self.Discount_rate = Discount_rate
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

    def discountPrice(self, price_info, Discount_rate):
        discounted_price = price_info - (price_info * Discount_rate / 100)
        return discounted_price


class InstockPush(WebPush):
    stock_info = bool

    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 stock_info):
        self.stock_info = stock_info
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

    def stockUpdate(self, stock_info):
        if stock_info == True:
            self.stock_info = False
        else:
            self.stock_info = True
        return self.stock_info


triggerPush = TriggerPush("Desktop", True, 3, "12.07.2019", "12.07.2021", "English", "Trigger", "cart")
print("Push Type: {}".format(triggerPush.push_type))
print(triggerPush.send_push())
bulkPush = BulkPush("Desktop", True, 3, "12.07.2019", "12.07.2021", "English", "Bulk", "12.20.23")
print("Push Type: {}".format(bulkPush.push_type))
print(bulkPush.send_push())
segmentPush = SegmentPush("Desktop", True, 3, "12.07.2019", "12.07.2021", "English", "Bulk", "new user")
print("Push Type: {}".format(segmentPush.push_type))
print(segmentPush.send_push())
priceAlertPush = PriceAlertPush("Desktop", True, 3, "12.07.2019", "12.07.2021", "English", "Price Alert", 1000, 15)
print("Push Type: {}".format(priceAlertPush.push_type))
print("DiscountPrice Method: {}".format(priceAlertPush.discountPrice(1000, 15)))
instockPush = InstockPush("Desktop", True, 3, "12.07.2019", "12.07.2021", "English", "In Stock", True)
print("InStockPush stock state before: {}".format(instockPush.stock_info))
instockPush.stockUpdate(instockPush.stock_info)
print("InStockPush stock state after: {}".format(instockPush.stock_info))
