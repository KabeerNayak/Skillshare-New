import sys, os
from skillshare import Skillshare, splash
# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    cookie = "device_session_id=614c7110-ecab-4a9b-ad76-bcf37a1af27e; show-like-copy=0; YII_CSRF_TOKEN=MGNuZWlIM1R5SmdxWW9xRWRUd01qWEJXUGdnVkNTV1MUvu5aOiqDyKjEor2t1a5eOgrEDVAP4MrugSCd4ME-Jw%3D%3D; visitor_tracking=utm_campaign%3D%26utm_source%3D%26utm_medium%3D%26utm_term%3D%26referrer%3Dhttps%3A%2F%2Fwww.google.com%2F%26referring_username%3D; first_landing=utm_campaign%3D%26utm_source%3D%26utm_medium%3D%26utm_term%3D%26referrer%3Dhttps%3A%2F%2Fwww.google.com%2F%26referring_username%3D; __stripe_mid=3d58c22b-6ebf-4bb4-8d77-9c4689f93986ce27b1; CAPTIONS=off; __stripe_sid=05699292-9b03-412a-9548-7f4accfeb096cc3f24; ss_hide_default_banner=1615618820.25; __cf_bm=08d54d242d46b6fd5b673f53621b1a882cd5b8e8-1616862073-1800-AT2az+4Rh+g5mCPPcwuxzbswR8V/hen9T915LHdMM280WjcJmGCtFAIVugHdw0H50d9l/sQK8v9I0mYQKH2RBi9alToQwsTihDwWdUj3T7fz; PHPSESSID=1bba9adab5943272d1f140dc004cad78; skillshare_user_=0c385bedf48d8157a6bba1eba065307c99ba796fa%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2218429968%22%3Bi%3A1%3Bs%3A22%3A%22kuqefyda%40conisocial.it%22%3Bi%3A2%3Bi%3A7776000%3Bi%3A3%3Ba%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A9%3A%22534794411%22%3Bs%3A10%3A%22login_time%22%3Bs%3A19%3A%222021-03-23%2003%3A13%3A56%22%3Bs%3A10%3A%22touch_time%22%3Bs%3A19%3A%222021-03-27%2016%3A21%3A30%22%3B%7D%7D"
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
