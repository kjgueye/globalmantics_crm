import os
import requests


def main():
    # Take user input for the message
    TEXT_TO_POST = input("Enter message: ")
    ROOM_NAME = "Karim's space"

    api_path = "https://webexapis.com/v1"

    # Retrieve the bearer token from environment variables
    bearer_token = os.environ.get("WT_API_TOKEN")
    if not bearer_token:
        raise ValueError("Use 'export WT_API_TOKEN=<token>' to access API")
    headers = {"Authorization": f"Bearer {bearer_token}"}

    # Debug: Print before making the GET request
    print("Fetching rooms...")

    try:
        get_rooms = requests.get(f"{api_path}/rooms", headers=headers, timeout=10)
        get_rooms.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching rooms: {e}")
        return

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

        # Debug: Print before making the POST request
        print("Posting message...")

        try:
            post_resp = requests.post(
                f"{api_path}/messages", headers=headers, json=body, timeout=10
            )
            post_resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error posting message: {e}")
            return

        log = post_resp.json()
        print(f"\nMessage '{log['text']}' posted by '{log['personEmail']}'")


if __name__ == "__main__":
    main()
