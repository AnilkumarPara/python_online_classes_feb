print("start")


def admin_required(func):
    def wrapper(user, *args, **kwargs):
        if not user.get('is_admin'):
            raise Exception("User must be an admin to access this function.")
        return func(*args, **kwargs)

    return wrapper


@admin_required
def delete_user():
    print("User deleted.")


admin_user = {"username": "adminuser", "is_admin": True}
regular_user = {"username": "regularuser", "is_admin": False}


delete_user(admin_user)


@admin_required
def update_user_role(user_id, new_role):
    # Assume this function updates the user's role in the database
    print(f"User {user_id}'s role has been updated to {new_role}.")


# Example users

# Trying to update a user's role with an admin user
update_user_role(admin_user, 123, "editor")


# Trying to update a user's role with a non-admin user
update_user_role(regular_user, 456, "editor")
