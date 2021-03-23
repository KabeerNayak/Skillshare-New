import sys, os
from skillshare import Skillshare, splash
# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    cookie = "device_session_id=179ae449-0d9a-4d29-83c7-d5211ebec7b5; show-like-copy=0; YII_CSRF_TOKEN=TzJBYVYzOU9nNDE1UDAxMEE5eUR4dVh6dzFIUGEwMEYvd50SrHBIc3k-PeXGONp4wDY5uIMLcJoxuQHUcYYfrw%3D%3D; visitor_tracking=utm_campaign%3D%26utm_source%3D%26utm_medium%3D%26utm_term%3D%26referrer%3Dhttps%3A%2F%2Fwww.google.com%2F%26referring_username%3D; first_landing=utm_campaign%3D%26utm_source%3D%26utm_medium%3D%26utm_term%3D%26referrer%3Dhttps%3A%2F%2Fwww.google.com%2F%26referring_username%3D; G_ENABLED_IDPS=google; __stripe_mid=29ad043e-e39a-4f65-97f4-56fdd02b694f5fc5f2; CAPTIONS=off; __stripe_sid=e112878e-3b76-4aea-ab36-6e46b61651b7b520e0; ss_hide_default_banner=1615618820.25; __cf_bm=21ab45d3154f67246e66da1c4239d2d8678a8437-1616428106-1800-AQOQjvzvDE8qCQNGSUqCumljC1qOPMqWvE9/T9wLrXfQ1OqSjwIiQu9J0ekJYuPS9GrhCqt9qC49Cy8L2IZ3gogFTmA6yaYj9eoOyr54V0y3; PHPSESSID=4079dc1588acfa1e3461c27911ccc20d; skillshare_user_=f716da727f21faa7fcebc6cab17e68ba2d2f1608a%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2218279032%22%3Bi%3A1%3Bs%3A22%3A%22whatisque3%40outlook.com%22%3Bi%3A2%3Bi%3A7776000%3Bi%3A3%3Ba%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A9%3A%22482183708%22%3Bs%3A10%3A%22login_time%22%3Bs%3A19%3A%222021-03-13%2007%3A00%3A13%22%3Bs%3A10%3A%22touch_time%22%3Bs%3A19%3A%222021-03-22%2015%3A48%3A31%22%3B%7D%7D"
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
