![alt text](https://github.com/antonsking/FriendBot-and-Friends/blob/main/FriendBot/icn/icn.png?raw=true)![alt text](https://github.com/antonsking/FriendBot-and-Friends/blob/main/FriendBot/icn/bicn.png?raw=true)![alt text](https://github.com/antonsking/FriendBot-and-Friends/blob/main/FriendBot/icn/icn.png?raw=true)
# FriendBot and Friends

A package of Instagram bots that interact with a target audience naturally, to efficiently and effectively return real and engaging followers. These include FriendBot, LikeBot, and UnfollowBot.

## Video Tutorial
FriendBot: https://youtu.be/KgBKQCPgGgI

UnfollowBot: https://youtu.be/wcFjy69-1Y8

LikeBot: Coming Soon


## How it Works

FriendBot performs social interactions on users posts. You supply FriendBot with other Instagram accounts that are similar in style to yours, and it will interact personally with their followers. These interactions consist of a follow, then 3-5 various interactions on their posts. These interactions include likes as well as comments.

FriendBot will not interact with a user if they have too many followers, or if they are following too many people. If the post has too many likes or comments FriendBot will skip it. FriendBot also checks their profile to make sure they post frequently and have followers, so they are not bot accounts. FriendBot will skip business accounts. 

To ensure your account doesnt get flagged, almost every parameter within the sourcecode of FriendBot is randomized constantly. Once FriendBot reaches the target interactions per hour, it will sleep until it can begin again.

UnfollowBot can be run once your follower count reaches around 200. It will time the follows exactly so that your account will not get flagged, and you maximise unfollow efficiency. It will begin with non-followers, and if left running for a long time, will begin to unfollow everyone. 


## Downloads and Dependencies

### .exe and .app coming soon

Please install Mozilla Firefox ( https://www.mozilla.org/ )

Please install Python 3.9 ( https://www.python.org/ ) and enable PATH

***IMPORTANT*** 
 Make sure your default Python version is 3.9 or above. Macs have default 2.7, and this ***will not work.***
 
 Once confirmed with ```python --version```, open the application "Terminal" and enter these two commands:
  
```
pip install caffeine
pip install instapy
```

 Download FriendBot here: https://github.com/antonsking/FriendBot-and-Friends/raw/main/FriendBot.zip 
 
 Download UnfollowBot here: https://github.com/antonsking/FriendBot-and-Friends/raw/main/UnfollowBot.zip
  
 Extract the zip anywhere, right click the enclosed ".command" file, and select "Open"
  

## Built With

* [InstaPy](https://instapy.org/) - A Selenium powered web scraper 
* [tkinter](https://docs.python.org/3/library/tkinter.html) - GUI
* [Caffeine](https://pypi.org/project/caffeine/) - To stay awake


## License

This Application is licensed under the CC0 1.0 Universal (CC0 1.0) -  ( https://creativecommons.org/publicdomain/zero/1.0/ )
