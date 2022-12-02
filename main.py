print('''
                           `.---...__
                           /```.__    ``.
 Pelecanus occidentalis    |```/  `'--.._`.
                           |``|        (o).)
                           \`` \    _,-'   `.
                            \```\  ( ( ` .   `.
                             `.```. `.` . `    `.
                               `.``\  `.__   `.  `.
                              ___\``), )\ `-.  `.  `.
                    __    _,-'   \,'  /  \   `-.  `. `.
                 ,-' '`,-'  '  ''| '   ' |      `-. `. `.
              ,-''_,-' '  ' '  ' |   '  '|         `-. `.`.
           ,-'_,-'   '   '  ''   | '  '  |            `-.`.`.
        ,-',-'  ''  ,'   |   |   |'   ' /                `-..`.
      ,' ,'  ' '     |  ,' | ,' /    ' '|                   `-.)
     // /  '   |    ,'    ,'   /   '  '/
     | || ,'  ,' |    ,' |   ,'   '   '|
     ||||   |   ,' ,'   ,' ,' ' '     /
     |  | |,'  '     |'  ,'  '   '  '/
     | ||,'   ,' |  ,' ,' '    \   '/
     ||||  |  , ,'  ,-'  /  ' '| ','
     | /  ,' '   ,-' '   |'    |,'
     | | ' ,' ,-' '  ' ' |    '|
     |||,' ,-'  '  '   '_|'  '/
     |,|,-' /'___,..--''  \ ' |
     / // ,'-' |' |        \  |
    ///,-'      \ |         \'|
   '--'          \'\        | |
               __ ) \___  __| |_
 ____,...----''   ||`-- <_.--._ -`--. __
  jrei            ''            `-`     `'''''''-----......_____
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
if (input("Left or right? ").lower() == 'left'):
  if (input("Swim or wait? ").lower() == 'wait'):
    tInput = input("Which door? ").lower()
    if (tInput == "red"):
      print("fire")
    elif (tInput == "yellow"):
      print("you win!")
    else: 
      print("eaten")
  else: print("trout")
else: print("hole")
