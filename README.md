# PythonInheritanceHomework
 
A class named WebPush has been defined. It has attributes named platform, optin, global_frequency_capping, start_date, end_date, language, push_type.
Classes named TriggerPush, BulkPush, SegmentPush, PriceAlertPush, InstockPush have been defined. The WebPush class has a function called send_push, and when this function is called, "Push sent!" is displayed. These classes inherit from the WebPush class. 


main class               inherit class                 methods                       variations                              type

web push                 triggerpush                                                 trigger_page                            string

web push                 bulkpush                                                    send_date                               integer

web push                 segmentpush                                                 segment_name                            string

web push                 pricealertpush             discountPrice()                  price_info, discount_rate               integer, float

web push                 instockpush                 stockUpdate()                   stock_info                              boolean



discountPrice(price_info, discount_rate) - This method will calculate the discount made on the product.
stockUpdate() - This method will update the stock information. For example, the stock information of the created object will be true with false, and true if false.
