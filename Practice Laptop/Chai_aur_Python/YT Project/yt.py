import json



def load_data():
    try:
        with open("youtube.txt","r") as f:
            return json.load(f)
        
    except FileNotFoundError:
        return []
        
def save_data_helper(videos):
    with open("youtube.txt","w") as f:       
        json.dump(videos,f)

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index ,video in enumerate(videos,start=1):
        
        
        print(f"{index}. {video['name']} , Duration: {video['time']}   ")

def add_video(videos):
     name=input("enter video name: ")
     time= input("enter video time: ")
     videos.append({"name":name ,"time":time })
     save_data_helper(videos)
     
     
 
def update_video(videos):
     list_all_videos(videos)
     index= int(input("enterr the video to update"))
     if 1<=index <=len(videos):
        name=input("enter the new video name :")
        time= input("enter the new video time :")
        videos[index-1]={'name':name,"time":time}
        save_data_helper(videos)
     else:
         print("invalid index selected")
         
        
def delete_video(videos):
     list_all_videos(videos)
     index=int(input("enter the video number to delete :"))
     if 1<=index<+len(videos):
         del videos[index-1]
     else:
         print(("invalid index selected"))


def main():
        
    videos=load_data()

    while True:
        print("\n Youtube Manager | Choose an Option")
        print("1. List all favourite videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice= int(input("enter a number: "))
        # print(videos)


        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case _:
                print("invalid choice")


if __name__ == "__main__":
    main()                
