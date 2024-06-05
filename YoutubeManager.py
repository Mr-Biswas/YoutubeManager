import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test= json.load(file)
            # print(type(test))
            return test
        
    except:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 80)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 80)

def add_video(videos):
    name= input("Enter Video Name: ").upper()
    time= input("Enter Video Duration: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index= int(input("Enter the Video number to Update: "))
    if 1<= index <= len(videos):
        name= input("Enter the video name: ").upper()
        time= input("Enter the duration of video: ")
        videos[index-1]={'name':name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid syntax")

def delete_video(videos):
    list_all_videos(videos)
    index= int(input("Enter the Video number to Delete: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid syntax")

def main():
    videos= load_data()
    while True:
        print("\n Youtube Manager | Choose ")
        print("1. List Your Favourite Videos ")
        print("2. Add Your Youtube VIdeos ")
        print("3. Update Any Video ")
        print("4. Delete Any Video ")
        print("5. Exit ")
        choice=input("Enter Your Choice: ")
        print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":

    main()


