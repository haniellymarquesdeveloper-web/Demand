from app.users.profiles import ProfileEnum

def can_close_demand(profile: ProfileEnum) -> bool:
    return profile in [ProfileEnum.ADMIN, ProfileEnum.GESTOR]
    