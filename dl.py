import sys, os
from skillshare import Skillshare, splash
# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    cookie = "device_session_id=614c7110-ecab-4a9b-ad76-bcf37a1af27e; show-like-copy=1; YII_CSRF_TOKEN=c435ed906f6676f46117f9a163f6f906d02fed2ea%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2218429968%22%3Bi%3A1%3Bs%3A22%3A%22kuqefyda%40conisocial.it%22%3Bi%3A2%3Bi%3A7776000%3Bi%3A3%3Ba%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A9%3A%22534794411%22%3Bs%3A10%3A%22login_time%22%3Bs%3A19%3A%222021-03-23%2003%3A13%3A56%22%3Bs%3A10%3A%22touch_time%22%3Bs%3A19%3A%222021-03-23%2003%3A15%3A00%22%3B%7D%7D; visitor_tracking=utm_campaign%3D%26utm_source%3D%26utm_medium%3D%26utm_term%3D%26referrer%3Dhttps%3A%2F%2Fwww.google.com%2F%26referring_username%3D; first_landing=utm_campaign%3D%26utm_source%3D%26utm_medium%3D%26utm_term%3D%26referrer%3Dhttps%3A%2F%2Fwww.google.com%2F%26referring_username%3D; __stripe_mid=3d58c22b-6ebf-4bb4-8d77-9c4689f93986ce27b1; CAPTIONS=off; __stripe_sid=98cf8723-b127-403d-bf8c-412497054b7f372082; ss_hide_default_banner=1615618820.25; __cf_bm=72c30ac65c5cdb18cad1f89503230a2e50eccfba-1616469240-1800-AWhf4ku9dI4Vhm+vr0VNH0gTWGblkQ1p3WbMbSWAmGM0huHN3KOva9fZ6g1kvM83/9UNGqq5N3ouVI882Y4PtaGs1pGfHVpEfS+mcfJsfwsuW2v2pZukMhjlT9HYLJG52/cq+4lCbWFUJoWWI2erctJyTm5xUxlhpse2oqDDJNmtlJJBtqswQ26WjBdiqMQwGQ==; PHPSESSID=d85d64894abc4bfb13d12150cf1f2c13; skillshare_user_=c435ed906f6676f46117f9a163f6f906d02fed2ea%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2218429968%22%3Bi%3A1%3Bs%3A22%3A%22kuqefyda%40conisocial.it%22%3Bi%3A2%3Bi%3A7776000%3Bi%3A3%3Ba%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A9%3A%22534794411%22%3Bs%3A10%3A%22login_time%22%3Bs%3A19%3A%222021-03-23%2003%3A13%3A56%22%3Bs%3A10%3A%22touch_time%22%3Bs%3A19%3A%222021-03-23%2003%3A15%3A00%22%3B%7D%7D"
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
