
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
    targets = creds[2]
    target_business_categories = ['art','lifestyle']

    
    ##########          COMMENTS           #########

    comments = ['awesome :ok_hand: @{}',
            'solid post :thumbsup:@{}',
            'absolutely dope :thumbsup:  @{}',
            'this is great :thumbsup:',
            ':thumbsup: very cool @{}?', 
            ':thumbsup: super cool @{}',
            'this is awesome @{}',
            'quality :ok_hand: @{}',
            ':raised_hands: awesome',
            'beastmode @{} :muscle:',
            ':thumbsup:this is cool',
            ':thumbsup:real sweet',
            'dope :thumbsup:',
            'this is awesome',
            'totally dope :thumbsup:  @{}',
            'great :thumbsup:',
            ':thumbsup: cool @{}?', 
            ':thumbsup: super cool @{}',
            'this is awesome @{}',
            'quality :ok_hand: @{}',
            ':raised_hands: awesome',
            'beastmode @{} :muscle:',
            ':thumbsup:this  cool',
            ':thumbsup: sweet',
            'so dope :thumbsup:',
            'this is awesome',
            'totally worth a follow :ok_hand:',
            'followed :thumbsup:',
            'defs worth a follow :ok_hand:',
            'def following :ok_hand:',
            'defs following :thumbsup:',
            'worth a follow :thumbsup:']





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


    ##################################     SETTINGS     ##################################################
        
        print("\n\n REMOVING UNFAVORABLES \n\n")
        #DELIMIT UNFAVORABLE POSTS 
        session.set_delimit_liking(enabled=True, max_likes=300, min_likes=None)
        session.set_delimit_commenting(enabled=True, max_comments=300, min_comments=None)

        #KEEP ACTIVITY IN CHECK
        session.set_simulation(enabled=True,percentage=85)

        session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments", "follows", "unfollows", "server_calls"],
                                   sleepyhead=True, stochastic_flow=True, notify_me=True,
                                   peak_comments_hourly=12,
                                   peak_comments_daily=160,#200 daily
                                   peak_follows_hourly=18, #peak 20 per hour
                                   peak_follows_daily=190, #peak 200 a day
                                   peak_unfollows_hourly=15, #both metrics included in follow
                                   peak_unfollows_daily=100, #^^^^
                                   peak_server_calls_hourly=190, ##limit 200
                                   peak_server_calls_daily=4700
                                     )  ##limit 4800
        

        ##DELIMIT TOO FAMOUS PPL AND BUSINESS ACCOUNTS
        session.set_relationship_bounds(enabled=True,
                                        potency_ratio=None,
                                        delimit_by_numbers=True,
                                        max_followers=2000,
                                        max_following=9000,
                                        min_followers=10,
                                        min_following=15,
                                        min_posts=2)
        
        session.set_skip_users(skip_private=True,
                               skip_no_profile_pic=True,
                               skip_business=True,
                               dont_skip_business_categories=[
                                   target_business_categories])
        

    ######      ENGAGEMENT       ##############################################################################
        print("\n\n SETTING \n\n")

        session.set_comments(comments)
        
        session.set_user_interact(amount=4, randomize=True, percentage=100)
        
        session.set_do_like(enabled=True, percentage=100)

        session.set_do_comment(enabled=True, percentage=18)

        
    ############################   TARGETED ACCOUNTS    ########################################################
        print("\n\n TARGETING \n\n")
        number = random.randint(5, 7)
        random_targets = targets

        if len(targets) <= number:
            random_targets = targets

        else:
            random_targets = random.sample(targets, number)


        #####################################    MAIN INTERACTION DRIVER    ########################################
        print("\n\n ENGAGING \n\n")
        session.follow_user_followers(random_targets,
                                      amount=10,
                                      randomize=True, sleep_delay=600,
                                      interact=True)


    ############################   UNFOLLOWING ROUTINE   ########################################################
        
        # UNFOLLOW activity

        session.unfollow_users(amount=random.randint(10, 150),
                               nonFollowers=True,
                               style="FIFO",
                               unfollow_after= 24 * 60 * 60, sleep_delay=600)

        session.unfollow_users(amount=random.randint(90, 150),
                               allFollowing=True,
                               style="FIFO",
                               unfollow_after= 48 * 60 * 60, sleep_delay=600)
        

        session.join_pods()

