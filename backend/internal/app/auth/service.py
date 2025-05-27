from sqlalchemy.orm import Session
from datetime import datetime
import uuid
from internal.models.mst_users import MstUsers
from internal.models.mst_userinfos import MstUserInfos
from internal.models.mst_user_roles import MstUserRoles
from utils.auth.hashing import hashing_password

def create_user():