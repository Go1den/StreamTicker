from slide import Slide

F_MOST_RECENT_SUBSCRIBER = "Streamlabs/most_recent_subscriber.txt"
F_SESSION_CHEER_AMOUNT = "Streamlabs/session_cheer_amount.txt"
F_SESSION_SUBSCRIBER_COUNT = "Streamlabs/session_subscriber_count.txt"
F_SESSION_TOP_CHEERER = "Streamlabs/session_top_cheerer.txt"
F_TOTAL_CHEER_AMOUNT = "Streamlabs/total_cheer_amount.txt"
F_TOTAL_SUBSCRIBER_COUNT = "Streamlabs/total_subscriber_count.txt"
F_TOTAL_SUBSCRIBER_SCORE = "Streamlabs/total_subscriber_score.txt"

S_LATEST_CHEER = Slide("bitimagefiles/bit10reduced.png", "Latest Cheer:", "", "", "", False)
S_MOST_RECENT_CHEERER = Slide("", "", "Streamlabs/most_recent_cheerer.txt", "", "", True)

S_LATEST_SUBSCRIBER = Slide("imagefiles/noWay.png", "Latest subscriber:", "", "", "", False)
S_MOST_RECENT_SUBSCRIBER_NAME = Slide("imagefiles/noWay.png", "", "Streamlabs/most_recent_subscriber.txt", "", "", False)

S_INSTAGRAM = Slide("imagefiles/insta.png", "Go1denDotCom")
S_TWITTER = Slide("imagefiles/twitter.png", "GoldenSRL")
S_YOUTUBE = Slide("imagefiles/youtube.png", "YouTube.com/GoldenSRL")
S_DISCORD = Slide("imagefiles/discord.png", "discord.gg/go1den")

MASTER_SLIDE_LIST = [S_INSTAGRAM, S_TWITTER, S_YOUTUBE, S_DISCORD]
