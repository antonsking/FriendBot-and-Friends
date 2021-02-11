
    ####################################################################################
    #
    #               _____ ______ _______ _______ _____ _   _  _____  _____ 
    #              / ____|  ____|__   __|__   __|_   _| \ | |/ ____|/ ____|
    #             | (___ | |__     | |     | |    | | |  \| | |  __| (___  
     #             \___ \|  __|    | |     | |    | | | . ` | | |_ |\___ \ 
     #             ____) | |____   | |     | |   _| |_| |\  | |__| |____) |
    #             |_____/|______|  |_|     |_|  |_____|_| \_|\_____|_____/ 
    #
    #
    ####################################################################################

import random
from instapy import InstaPy
from instapy import smart_run

def bot(creds):

    #########          CREDENTIALS           ############
    insta_username = creds[0]
    insta_password = creds[1]


    ##########      TARGET USERS - ACCOUNTS SIMILAR TO YOURS       #########



    ####################################################################################
    #             
    #              _____ ______  _____ _____ _____ ____  _   _ 
    #              / ____|  ____|/ ____/ ____|_   _/ __ \| \ | |
    #             | (___ | |__  | (___| (___   | || |  | |  \| |
    #              \___ \|  __|  \___ \\___ \  | || |  | | . ` |
    #              ____) | |____ ____) |___) |_| || |__| | |\  |
    #             |_____/|______|_____/_____/|_____\____/|_| \_|
    #
    #
    ####################################################################################
    print("\n\n CREATING SESSION \n\n")
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=True,
                      disable_image_load=True,
                      multi_logs=True)

    with smart_run(session):

        #KEEP ACTIVITY IN CHECK
        session.set_simulation(enabled=True,percentage=100)

        session.set_quota_supervisor(enabled=True, sleep_after=["unfollows", "server_calls"],
                                   sleepyhead=True, stochastic_flow=True, notify_me=True,
                                   peak_unfollows_hourly=18, #both metrics included in follow
                                   peak_unfollows_daily=150, #^^^^
                                   peak_server_calls_hourly=190, ##limit 200
                                   peak_server_calls_daily=4700
                                     )  ##limit 4800
        
    ############################   UNFOLLOWING ROUTINE   ########################################################
        
        # UNFOLLOW activity

        session.unfollow_users(amount=180,
                               nonFollowers=True,
                               style="FIFO",
                               unfollow_after=1)

        session.unfollow_users(amount=100,
                               allFollowing=True,
                               style="FIFO",
                               unfollow_after= 24 * 60 * 60)
        

        session.join_pods()

