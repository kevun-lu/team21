# team21
|  GitName | Student |
|----------|---------|
|Astr0Jay|Justin Anderson|
|yukiikebe|Yuki Ikebe|
|takekikawate|Takeki Kawate|
|kevun-lu| Kevin Lu|
|jacobround|Jacob Round|
|kevv10|Kevin Van|


Necessary python package installations:
tkinter
supabase
dotenv
pillow

Run with python 3.12
Splash screen and Player entry screen will run from the command "python3 main.py"

To use the player entry screen, input your first codename id on the leftmost column on each team. Then click "search" for that team.
As of 3/17/2024, there are four ids currently used: 1, 2, 3, 4, 5. After you click search, the corresponding codename will appear in the middle column. If you use a new id, then it will display need "new code_name" instead. Type in a new codename in the box it appears in and then click the "update" button for that team. This will then send the codename to the database and will appear next time that id is used. Afterwards, input the equipment id on the rightmost column on the team and press ok. Repeat this process for every player then press "start game". A startup countdown will then popup and will the play action screen appear once it finishes.

Prior to starting the server first check the LOCAL_IP and LOCAL_PORT variables in the code.
If you skip that first step it will be near impossible to achieve successful udp communication.
To run the udp server run the command "python3 UDP_Server.py".
Then each client will need to run the command "python3 UDP_Client.py".
Once all the players are connected to the udp server press f3 to lock in the equipment and start the game.
