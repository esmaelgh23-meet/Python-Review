def create_youtube_video(title,description):
  youtube_video = {"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}
  return youtube_video


def like (youtube_video):
  if "likes" in youtube_video:
    youtube_video["likes"]+=1
    return youtube_video


def dislike (youtube_video):
  if "dislikes" in youtube_video:
    youtube_video["dislikes"]+=1
    return youtube_video

def add_comment(youtube_video,username,comment_text):
  youtube_video["comments"][username]= comment_text
  return youtube_video

new_video=create_youtube_video("messi goal","great player")
new_video=add_comment(new_video,"Esmael","ghjfafjh")

print (new_video)

for x in range(495):
  new_video=like(new_video)

new_video=dislike(new_video)


print (new_video)









# comments=create_function{username:text}


# if (likes in new_function)
#     likes=likes+1
#  else
#      likes=null

# #change student_1
# def create_like(new_function,likes):
#   student = {“Name”:name,”Year”:year,”Gender”:gender}
#   return create_like

# def create_dislike(new_function,likes):
#   student = {“Name”:name,”Year”:year,”Gender”:gender}
#   return create_like

# def (new_function,likes):
#   student = {“Name”:name,”Year”:year,”Gender”:gender}
#   return create_like


























