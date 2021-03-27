import sys, os
from skillshare import Skillshare, splash
# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    cookie = "_uetvid=91d92d9076a911ebb43f255bf8a498d9;YII_CSRF_TOKEN=MGNuZWlIM1R5SmdxWW9xRWRUd01qWEJXUGdnVkNTV1MUvu5aOiqDyKjEor2t1a5eOgrEDVAP4MrugSCd4ME-Jw%3D%3D;IR_gbd=skillshare.com;__utmc=99704988;_sctr=1|1615910400000;__stripe_mid=3d58c22b-6ebf-4bb4-8d77-9c4689f93986ce27b1;_derived_epik=dj0yJnU9bGdtY2NveDUxbWVNY3FrOWt3Y0ZjOUh4Y0ZMbDVOLVgmbj1xTTJrN1ZESkVMdDFUN09IdUo2QUhBJm09MSZ0PUFBQUFBR0JaWFRRJnJtPTEmcnQ9QUFBQUFHQlpYVFE;IR_PI=9bba9974-76a9-11eb-aac6-025ecbc6e250%7C1616555699200;__utma=99704988.1723270278.1614175624.1615935448.1616469065.19;__ssid=320827a2729ea9717fe628d3be6c933;__pdst=63159d98cf1f4fadb0f28af4a52bc5d0;__qca=P0-1151002195-1614175627129;__utmv=99704988.|1=visitor-type=user=1;__utmz=99704988.1614175624.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);_ga=GA1.2.1723270278.1614175624;_gcl_au=1.1.1184408361.1614175622;_pin_unauth=dWlkPU9ERTVaV1V5T0dZdFpETmtZaTAwTVRVM0xUbGhZVGd0Wm1SbE1XSTRZekEyTWpjNQ;_scid=487f75b2-8439-460b-8b8c-87742e2074c5;device_session_id=614c7110-ecab-4a9b-ad76-bcf37a1af27e;first_landing=utm_campaign%3D%26utm_source%3D%26utm_medium%3D%26utm_term%3D%26referrer%3Dhttps%3A%2F%2Fwww.google.com%2F%26referring_username%3D;G_ENABLED_IDPS=google;IR_4650=1616469299200%7C0%7C1616469066620%7C%7C;sm_uuid=1614175991484;__cfduid=d5b62300b9e50e89ef237c3e1b3f4b97e1616862073;show-like-copy=0;visitor_tracking=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D;__stripe_sid=b8a7c0e7-146f-471f-8f45-d7128998bb58722238;dismiss_transcripts_tooltip=1;ss_hide_default_banner=1616866390.129;__cf_bm=9af2a61e74edfbcf16d7840c37f2043fcb0504ba-1616867198-1800-AYb1H/l73kLSKb8Xthub9vi5oIxDHm2PebbTa2u/99lAQ6X561zyzNfjmMrDDnK/nxO8K7V4zG6mSxtDo40wEySLyLyfu+0RC63bg0pVwZi9;PHPSESSID=119b8f6ab7adb7bbb62fe644e5660156;skillshare_user_=904a926df08fe87d2f65c1dcbbdf58526ea50e06a%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2218429968%22%3Bi%3A1%3Bs%3A22%3A%22kuqefyda%40conisocial.it%22%3Bi%3A2%3Bi%3A7776000%3Bi%3A3%3Ba%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A9%3A%22534794411%22%3Bs%3A10%3A%22login_time%22%3Bs%3A19%3A%222021-03-23%2003%3A13%3A56%22%3Bs%3A10%3A%22touch_time%22%3Bs%3A19%3A%222021-03-27%2017%3A55%3A26%22%3B%7D%7D"
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
