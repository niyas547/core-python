from blogapplication.models import users,blogs
print(len(users))
print(len(blogs))
# 1
most_liked=max(blogs,key=lambda like:len(like.get("liked_by")))
print(most_liked)
# 2
low_following=min(users,key=lambda low:len(low.get("following")))
print(low_following)
# 3
post_spec_user=[user for user in blogs if user.get("userId")==2]
print(post_spec_user)
# 4 followers of a specific user
userId=1
foll_spe_user=[user.get("username") for user in users if userId in user.get("following")]
print(foll_spe_user)
# 5authentication
user_name="akhil"
pswrd="Password@123"
user=[ user for user in users if user.get("username")==user_name and user.get("password")==pswrd]
print(user)
if len(user)>0:
    print("login success")
else:
    print("invalid credentials!!!!!!...")
# 6 which user is uploaded most no of posts
blog_count={}
for blog in blogs:
    user_id=blog.get("userId")
    user_name=[user.get("username") for user in users if user.get("id")==user_id].pop()
    if user_name in blog_count:
        blog_count[user_name]=blog_count[user_name]+1
    else:
        blog_count[user_name]=1
print(blog_count)
max_post=max(blog_count,key=lambda k:blog_count[k])
print("user with most no:of posts=",max_post)
#7 more active user
like_count={}
for blog in blogs:
    user_liked=blog.get("liked_by")
    for user in user_liked:
        if user in like_count:
            like_count[user]+=1
        else:
            like_count[user]=1
print(like_count)
max_liked=max(like_count,key=lambda k:like_count[k])
print([user.get("username") for user in users if user.get("id")==max_liked].pop())
#8 user name along with number of post
# SAME AS 6TH QUESTION
#9 sort along with count of following
users.sort(key=lambda u:len(u.get("following")),reverse=True)
print(users)
# reverse=True decsending order sorting
#10 print invitation to follow for specific user  (suggestions)
loged_user=6
all_users=[user.get("id") for user in users ]
all_users.remove(loged_user)
print("user id of all users=",all_users)
loged_user_following=[user.get("following") for user in users if user.get("id")==loged_user].pop()
print("user id of the following users=",loged_user_following)
print("user id to follow the user=",set(all_users)-set(loged_user_following))

# pop( ) to remove the list of list