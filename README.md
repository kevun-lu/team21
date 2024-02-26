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


To use the player entry screen, input all ids for a team in the left column first, then click the search button for that team.
As of 2/25/2024, there are four ids currently used: 1, 2, 3, 4. After you click search, the corresponding codenames will appear in the right column.
If you use a new id, then it will display need new code_name instead. For these players, type in all of their codenames and then click the update 
button for that team. This will then send those new ids and codenames to the database and will appear next time those ids are used.


Prior to starting the server first check the LOCAL_IP and LOCAL_PORT variables in the code.
If you skip that first step it will be near impossible to achieve successful udp communication.
To run the udp server run the command "python3 UDP_Server.py".
Then each client will need to run the command "python3 UDP_Client.py".
Once all the players are connected to the udp server press f3 to lock in the equipment and start the game.
