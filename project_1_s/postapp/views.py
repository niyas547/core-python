from postapp.models import users,blogs
session={}
class Login:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=[user for user in users if user.get("username")==username and user.get("password")==password]
        if user:
            session["user"]=user.pop()
            print("Login Success")
        else:
            print("Invalid Credentails!!!!!!!")
# def Logout():
#     if "user" in session:
#         session.pop("user")
#     else:
#         print("Operation not allowed!!!!!!!")
class PostList:
    def get(self,*args,**kwargs):
        if "user" in session:
            return blogs
        else:
            return "u must login"
    def post(self,*args,**kwargs):
        data=kwargs.get("data")
        if "user" in session:
            id=session["user"]["id"]
            data["userId"]=id
            blogs.append(data)
            print("post has been created")
            print(blogs)
        else:
            print("u must login")

class MyPostList:
    def get(self,*args,**kwargs):
        if "user" in session:
            userId=session["user"]["id"]
            posts=[blog for blog in blogs if blog.get("userId")==userId]
            print(posts)
        else:
            print("u must login!!!!")

class PostDetails:
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        if "user" in session:
            post=[blog for blog in blogs if blog.get("postId")==post_id].pop()
            print("The Post Is=",post)
        else:
            print("U Must Login")

    def delete(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        if "user" in session:
            post=[blog for blog in blogs if blog.get("postId")==post_id].pop()
            blogs.remove(post)
            print(blogs)
        else:
            print("u must login!!!!!")
    def put(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=kwargs.get("data")
        post=[blog for blog in blogs if blog.get("postId")==post_id].pop()
        post.update(data)
        print(blogs)


auth=Login()
auth.post(username="nikil",password="Password@123")
post=PostDetails()
# post.get(post_id=1)
# post.delete(post_id=2)
post.put(post_id=3,data={"postId": 3, "userId": 1, "title": "how are you", "content": "content", "liked_by": [1, 2, 3,5]})

# post=MyPostList()
# post.get()
# posts=PostList()
# print(posts.get())
# data= {"postId": 10, "title": "goodmorning", "content": "content"}
# posts.post(data=data)




# print("session before logout")
# print(session)
# Logout()
# print("session after logout")
# print(session)







# class UsersView:
#     def get(self):
#         return users
#     def post(self,*args,**kwargs):
#         user=kwargs.get("data")
#         users.append(user)
#         return user
# all_user=UsersView()
# print(all_user.get())
# data= {"id": 11, "username": "ram", "email": "ram@gmail.com", "password": "Password@123"}
# print(all_user.post(data=data))
#
# class UserDetails:
#     def get(self,*args,**kwargs):
#         id=kwargs.get("id")
#         data1=[user for user in users if user.get("id")==id]
#         return data1
#

# user_detail=UserDetails()
# print(user_detail.get(id=1))
