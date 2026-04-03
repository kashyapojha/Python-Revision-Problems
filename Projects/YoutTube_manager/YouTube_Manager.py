import json

# Load data from file
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save data to file
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)

# List all videos
def list_all_videos(videos):
    if not videos:
        print("No videos found.")
        return

    print("\n--- Your Videos ---")
    for i, vid in enumerate(videos, start=1):
        print(f"{i}. Name: {vid['name']} | Time: {vid['time']}")

# Add new video
def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("Video added successfully!")

# Update video
def update_videos(videos):
    list_all_videos(videos)
    
    try:
        index = int(input("Enter video number to update: ")) - 1
        if 0 <= index < len(videos):
            name = input("Enter new name: ")
            time = input("Enter new time: ")

            videos[index] = {'name': name, 'time': time}
            save_data_helper(videos)
            print("Video updated successfully!")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete video
def delete_videos(videos):
    list_all_videos(videos)
    
    try:
        index = int(input("Enter video number to delete: ")) - 1
        if 0 <= index < len(videos):
            deleted = videos.pop(index)
            save_data_helper(videos)
            print(f"Deleted video: {deleted['name']}")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function
def main():
    videos = load_data()

    while True:
        print("\n📺 YouTube Manager")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                print("Exiting... Goodbye!")
                break
            case _:
                print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()