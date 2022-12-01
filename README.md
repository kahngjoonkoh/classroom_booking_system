# classroom_booking_system
A web server that will allow users to book empty classrooms.

## System Flow
<img width="700" alt="image" src="https://user-images.githubusercontent.com/46638829/205007299-9cabe9bf-4c87-424f-b095-b5b5a6aa938e.png">

1. Enters initial information that updates the database as in the available classrooms, the time periods, the available equipments, and user credentials that could be used to validate the end user.
2. Starts the Flask server. Also generates a QR code (or equivalent) that enables user access.
3. End users will use scan the QR code that will redirect them to the webpage hosted by the server.
4. End users will enter information such as their school ID and name for basic validation. This information will be hashed. Also, the user will query what rooms they want to book at a specific time with the equipment they have selected. Possibly, it could ask for the purpose of using the room.
5. The server queries the database with the information received from the user. 
6. The database returns information.
7. Based on what the database returned, the server will display appropriate responses to the user such as, telling whether the booking was successful or not.
