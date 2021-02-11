![alt text](https://github.com/antonsking/FriendBot-and-Friends/blob/main/FriendBot/icn/icn.png?raw=true)![alt text](https://github.com/antonsking/FriendBot-and-Friends/blob/main/FriendBot/icn/bicn.png?raw=true)![alt text](https://github.com/antonsking/FriendBot-and-Friends/blob/main/FriendBot/icn/icn.png?raw=true)
# FriendBot and Friends

A package of Instagram bots that interact with a target audience naturally, to efficiently and effectively return real and engaging followers. These include FriendBot, LikeBot, and UnfollowBot.


## How it Works

FriendBot performs social interactions on users posts. You supply FriendBot with other Instagram accounts that are similar in style to yours, and it will interact personally with their followers. These interactions consist of a follow, then 3-5 various interactions on their posts. After 24 hours, nonfollowers are unfollowed, and after 48, all followers are. These interactions include likes as well as comments.

FriendBot will not interact with a user if they have too many followers, or if they are following too many people. This is to make sure users that are interacted with are the type that will return a follow. Furthermore, if thier post has too many likes or comments FriendBot will skip it, as this interaction is less meaningful to the user. FriendBot also checks their profile and makes sure they post frequently and have followers, to ensure they are not bot accounts. FriendBot will skip business accounts. 

Most Instagram bots return fake followers, which do not interact with your posts, leaving you with a high follower count and low post interactions. The followers that FriendBot returns are active, engaging, and most importantly real. 

To ensure your account doesnt get flagged, almost every parameter within the sourcecode of FriendBot is randomized constantly. Once FriendBot reaches the target interactions per hour, it will sleep until it can begin again.


## Downloads and Dependencies

### .exe and .app coming soon

Please install Mozilla Firefox ( https://www.mozilla.org/ )

Please install Python 3.9 ( https://www.python.org/ ) and enable PATH

***IMPORTANT*** 
 Make sure your default Python version is 3.9 or above. Macs come default with 2.7, and this ***will not work.***
 
 Once copleted and confirmed with ```python --version```, open the application "Terminal" and type these two commands:
  
```
pip install caffeine
pip install instapy
```

 Download FriendBot here: https://bit.ly/2MUWklg 
  
 Extract the zip anywhere, right click the enclosed "InstaBotApp.command" file, and select "Open"
  

## Built With

* [InstaPy](https://instapy.org/) - The Selenium based web scraper used
* [tkinter](https://docs.python.org/3/library/tkinter.html) - For the GUI
* [Caffeine](https://pypi.org/project/caffeine/) - To stay awake


## License

This Application is licensed under the CC0 1.0 Universal (CC0 1.0) -  ( https://creativecommons.org/publicdomain/zero/1.0/ )
