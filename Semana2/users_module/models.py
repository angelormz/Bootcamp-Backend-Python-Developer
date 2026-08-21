if __name__ == "__main__":
    viewer = Role(name="viewer", permissions=["read_tasks"])
    user = User(name="Ana", email="ana@taskflow.com", role=viewer)
    admin = Admin(name="Beto", email="beto@taskflow.com", role=Role("admin", ["read_tasks"]))

    print(user)
    print("¿Ana puede borrar?", user.can("delete_tasks"))
    print("¿Beto administra usuarios?", admin.can("manage_users"))