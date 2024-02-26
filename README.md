# team21
|  GitName | Student |
|----------|---------|
|Astr0Jay|Justin A.|
|yukiikebe|Yuki I.|
|takekikawate|Takeki K.|
|kevun-lu| Kevin L.|
|jacobround|Jacob R.|
|kevv10|Kevin V.|

software-engineering group: takeki, jacob, yuki, kevin^2, Justin

Necessary python package installations:
tkinter
supabase
dotenv
pillow

Run with python 3.12
Splash screen and Player entry screen will run from the command "python3 main.py"


Prior to starting the server first check the LOCAL_IP and LOCAL_PORT variables in the code.
If you skip that first step it will be near impossible to achieve successful udp communication.
By default both IP addresses are set to "localhost"
To run the udp server run the command "python3 UDP_Server.py".
Then each client will need to run the command "python3 UDP_Client.py".
Once all the players are connected to the udp server press f3 to lock in the equipment and start the game.
