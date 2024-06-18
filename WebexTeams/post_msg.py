import os
import requests

def main():

    TEXT_TO_POST = "This is the live demo for real!!!"
    ROOM_NAME = "Karim's space"


    api_path = "https://webexapis.com/v1"


    bearer_token = "YjhlNWE2YmYtYjcyOS00ODIzLWI3NWQtOWNkY2ExMDYyNDEwMGNmYTZkYWUtMmZj_P0A1_9db452ae-a8fa-4c45-ad97-a9c6809f2db1"
    if not bearer_token:
        raise ValueError("Use 'export WT_API_TOKEN=<token>' to access API")
    headers = {"Authorization": f"Bearer {bearer_token}"}


    get_rooms = requests.get(f"{api_path}/rooms", headers=headers)

    get_rooms.raise_for_status()
    rooms = get_rooms.json()



    internal_room_id = None
    for room in rooms["items"]:
        if ROOM_NAME.lower() in room["title"].lower():
            print("Room information")
            print(f"  Title: {room['title']}")
            print(f"  ID: {room['id']}")
            internal_room_id = room["id"]
            break

    if internal_room_id:
        body = {"roomId": internal_room_id, "text": TEXT_TO_POST}
        post_resp = requests.post(
            f"{api_path}/messages", headers=headers, data=body
        )
        post_resp.raise_for_status()
        log = post_resp.json()
        print (f"\nMessage '{log['text']}' posted by '{log['personEmail']}")

if __name__ == "__main__":
    main()